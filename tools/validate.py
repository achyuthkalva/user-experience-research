#!/usr/bin/env python3
"""Check this release's known format, content inventory, links, and archives.

This is a project-specific static checker, not the Agent Skills reference
validator, a legal/privacy audit, or an LLM behavioural evaluation.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]


def validate() -> list[dict[str, object]]:
    c = json.loads((ROOT / "release.json").read_text(encoding="utf-8"))
    v, name = c["version"], c["name"]
    skill = ROOT / "skills" / name
    dist = ROOT / "dist"
    results: list[dict[str, object]] = []
    def check(label: str, ok: bool, detail: str = "") -> None:
        results.append({"check": label, "passed": bool(ok), "detail": detail})
    core = (skill / "SKILL.md").read_text(encoding="utf-8")
    front = re.match(r"\A---\nname: ([^\n]+)\ndescription: (\"[^\n]+\")\n---\n", core)
    check("Required YAML-frontmatter structure", front is not None)
    if front:
        desc = json.loads(front.group(2))
        check("Name and directory convention", bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)) and len(name) <= 64 and front.group(1) == name)
        check("Description length", 1 <= len(desc) <= 1024, f"{len(desc)} characters")
    check("Compact core", len(core.splitlines()) < 500, f"{len(core.splitlines())} lines")
    runtime = sorted(p for p in skill.rglob("*") if p.is_file())
    check("Runtime is text-only with no symlinks", all(p.suffix in {".md", ".txt"} and not p.is_symlink() and b"\x00" not in p.read_bytes() for p in runtime))
    check("Eleven reference modules", len(list((skill / "references").glob("*.md"))) == 11)
    template_text = (skill / "references" / "08-templates.md").read_text(encoding="utf-8")
    template_ids = re.findall(r"^## T(\d+)\b", template_text, re.M)
    check("Twelve complete template headings", template_ids == [str(i) for i in range(1, 13)])
    cal = (skill / "references" / "10-sources.md").read_text(encoding="utf-8")
    check("Twenty-one explicit calibration records", set(re.findall(r"\| (C\d{2}) \|", cal)) == {f"C{i:02d}" for i in range(1, 22)})
    link_errors = []
    for p in sorted(ROOT.rglob("*.md")):
        if any(x in p.relative_to(ROOT).parts for x in ["dist", "__pycache__", ".git"]):
            continue
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", p.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            resolved = (p.parent / target.split("#", 1)[0]).resolve()
            if not resolved.is_relative_to(ROOT.resolve()) or not resolved.exists():
                link_errors.append(f"{p.relative_to(ROOT)} -> {target}")
    check("Local Markdown links resolve", not link_errors, "; ".join(link_errors))
    source_text = "\n".join(p.read_text(encoding="utf-8") for p in runtime)
    private_patterns = [r"https?://(?:app\.)?notion\.(?:so|com)/", r"https?://[^\s/]+\.notion\.site/", r"collection://", r"user://", r"X-Amz-Signature=", r"sk-[A-Za-z0-9]{20,}"]
    check("No matched private-source/credential patterns in runtime", not any(re.search(p, source_text) for p in private_patterns), "Limited pattern scan; not a complete security audit")
    check("Core preserves ordered OMSEP and H3", "Objective → Methodology → Scope → Essentials → Protocol" in core and "H3 — Priority and action order: HARD STOP" in core)
    check("Current version in runtime entry documents", all(v in (skill / p).read_text(encoding="utf-8") for p in ["SKILL.md", "SETUP.md", "START-HERE.md"]))
    txt_path = dist / f"UX-Research-Chat-v{v}.txt"
    if txt_path.exists():
        txt = txt_path.read_text(encoding="utf-8")
        check("Flat edition embeds every runtime file", all(f"## Embedded file: {p.relative_to(skill).as_posix()}\n" in txt for p in runtime))
        check("Flat edition end marker", txt.rstrip().endswith(f"END-OF-PACKAGE: UX-RESEARCH-{v}"))
        check("TXT and Markdown editions identical", txt_path.read_bytes() == (dist / f"UX-Research-Chat-v{v}.md").read_bytes())
        anchors = set(re.findall(r'<a id="([^"]+)"></a>', txt))
        links = re.findall(r"\]\(#(file-[^)]+)\)", txt)
        check("Flat edition navigation resolves", all(a in anchors for a in links))
    else:
        check("Flat edition exists", False, "Run tools/build.py first")
    for filename, prefix in [(f"{name}-v{v}.skill", f"{name}/"), (f"{name}-gemini-v{v}.zip", "")]:
        path = dist / filename
        if not path.exists():
            check(f"Archive exists: {filename}", False)
            continue
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            safe = len(names) == len(set(names)) and all(not PurePosixPath(n).is_absolute() and ".." not in PurePosixPath(n).parts and "\\" not in n for n in names)
            safe &= all(((i.external_attr >> 16) & 0o170000) != 0o120000 for i in z.infolist())
            check(f"Safe archive layout: {filename}", safe and z.testzip() is None)
            expected = {prefix + p.relative_to(skill).as_posix(): p.read_bytes() for p in runtime}
            check(f"Archive is complete and matches canonical files: {filename}", set(names) == set(expected) and all(z.read(n) == b for n, b in expected.items()))
    a, b = dist / f"{name}-v{v}.skill", dist / f"{name}-v{v}.zip"
    check("Skill and folder ZIP byte-identical", a.exists() and b.exists() and a.read_bytes() == b.read_bytes())
    checksums = dist / "CHECKSUMS.sha256"
    valid_hashes = checksums.exists()
    if valid_hashes:
        for line in checksums.read_text().splitlines():
            digest, filename = line.split("  ", 1)
            p = dist / filename
            valid_hashes &= p.exists() and hashlib.sha256(p.read_bytes()).hexdigest() == digest
    check("Release checksums match", bool(valid_hashes))
    cases = json.loads((ROOT / "tests" / "scenarios.json").read_text(encoding="utf-8"))
    check("Twenty-four unique model-evaluation specifications", len(cases) == 24 and len({x["id"] for x in cases}) == 24 and all(x["status"] == "not-run" for x in cases))
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        results = validate()
        if args.json:
            print(json.dumps({"checks": results, "live_model_tests": "not-run"}, indent=2))
        else:
            for row in results:
                print(f"{'PASS' if row['passed'] else 'FAIL'}  {row['check']} {row['detail']}")
            print(f"\n{sum(r['passed'] for r in results)}/{len(results)} static checks passed. Model tests: NOT RUN.")
        raise SystemExit(0 if all(x["passed"] for x in results) else 1)
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
