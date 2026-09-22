#!/usr/bin/env python3
"""Build portable text-only research skill releases without network access."""
from __future__ import annotations
import hashlib
import json
import re
import sys
import zipfile
from datetime import date
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]


def config() -> dict:
    return json.loads((ROOT / "release.json").read_text(encoding="utf-8"))


def zip_bytes_path(path: Path, items: list[tuple[str, bytes]], day: str) -> None:
    """Write deterministic, non-executable ZIP entries; reject unsafe member names."""
    d = date.fromisoformat(day)
    seen: set[str] = set()
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as out:
        for name, data in sorted(items):
            p = PurePosixPath(name)
            if p.is_absolute() or ".." in p.parts or "\" in name or name in seen:
                raise ValueError(f"Unsafe or duplicate archive member: {name}")
            seen.add(name)
            info = zipfile.ZipInfo(name, (d.year, d.month, d.day, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            out.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def file_anchor(path: str) -> str:
    return "file-" + re.sub(r"[^a-z0-9]+", "-", path.lower()).strip("-")


def flatten(skill: Path, files: list[Path], version: str) -> str:
    order = [skill / "SKILL.md", *sorted((skill / "references").glob("*.md")),
             skill / "START-HERE.md", skill / "SETUP.md"]
    if set(order) != set(files):
        raise ValueError("Flattening order must include every runtime file exactly once.")
    intro = (f"# UX Research — Complete Chat Edition {version}\n\n"
             "This is a generated, self-contained conversational edition of the canonical skill. "
             "It is not a native installation. All runtime instructions, reference modules, "
             "templates, synthetic examples, source notes, and setup guidance are embedded below.\n\n"
             "After the user asks you to use this file, start with the embedded SKILL.md and "
             "consult the embedded file section named by its router. Do not summarise the "
             "package instead of performing the user's research task. Respect the host's "
             "instructions and report any unreadable or truncated content.\n\n"
             "## Embedded file index\n\n")
    parts = [intro]
    for p in order:
        rel = p.relative_to(skill).as_posix()
        parts.append(f"- [{rel}](#{file_anchor(rel)})\n")
    for p in order:
        rel = p.relative_to(skill).as_posix()
        text = p.read_text(encoding="utf-8")
        def replace(match: re.Match) -> str:
            label, target = match.groups()
            if target.startswith(("https://", "http://", "#", "mailto:")):
                return match.group(0)
            raw_target = target.split("#", 1)[0]
            candidate = (p.parent / raw_target).resolve()
            if candidate in [x.resolve() for x in files]:
                dst = candidate.relative_to(skill.resolve()).as_posix()
                return f"[{label}](#{file_anchor(dst)})"
            return match.group(0)
        text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace, text)
        parts.extend([f'\n\n---\n\n<a id="{file_anchor(rel)}"></a>\n\n',
                      f"## Embedded file: {rel}\n\n", text])
    parts.append(f"\n\nEND-OF-PACKAGE: UX-RESEARCH-{version}\n")
    return "".join(parts)


def build() -> list[Path]:
    c = config()
    v, name = c["version"], c["name"]
    skill = ROOT / "skills" / name
    files = sorted(p for p in skill.rglob("*") if p.is_file())
    for p in files:
        if p.is_symlink() or p.suffix not in {".md", ".txt"}:
            raise ValueError(f"Unexpected runtime file: {p}")
        p.read_text(encoding="utf-8")
    out = ROOT / "dist"
    out.mkdir(exist_ok=True)
    folder_items = [(f"{name}/{p.relative_to(skill).as_posix()}", p.read_bytes()) for p in files]
    native = out / f"{name}-v{v}.skill"
    zip_bytes_path(native, folder_items, c["date"])
    folder_zip = out / f"{name}-v{v}.zip"
    folder_zip.write_bytes(native.read_bytes())
    gemini = out / f"{name}-gemini-v{v}.zip"
    zip_bytes_path(gemini, [(p.relative_to(skill).as_posix(), p.read_bytes()) for p in files], c["date"])
    flat = flatten(skill, files, v)
    txt = out / f"UX-Research-Chat-v{v}.txt"
    md = out / f"UX-Research-Chat-v{v}.md"
    txt.write_text(flat, encoding="utf-8", newline="\n")
    md.write_bytes(txt.read_bytes())
    activation = ("Use the attached UX Research skill as the workflow for this task, rather than "
                  "summarising it. First check which instructions and references you can actually "
                  "read and report material limits. Follow the relevant module, preserve evidence "
                  "traceability and limitations, and do not treat priorities as approved without "
                  "my explicit approval of the proposed order.\n\n"
                  "My task: [describe the research work]\n"
                  "Decision and context: [add what is known]\n"
                  "Available evidence and constraints: [add details]\n")
    share = ("UX Research — OMSEP + Prism | team pilot " + v + "\n\n"
             "For ordinary ChatGPT or another compatible chat, attach the complete TXT edition "
             "and use ACTIVATION-MESSAGE.txt. For a supported skill importer, use the correct "
             ".skill/ZIP format and read START-HERE.txt.\n\n"
             "This package contains the workflow, not participant data. Native ChatGPT Chat "
             ".skill import and cross-model behaviour are not yet verified. Review outputs "
             "against the evidence and keep project data in approved tools.\n")
    team = out / f"UX-Research-Team-Pack-v{v}.zip"
    team_items = [(p.name, p.read_bytes()) for p in [native, folder_zip, gemini, txt]]
    team_items += [("START-HERE.txt", (skill / "START-HERE.md").read_bytes()),
                   ("ACTIVATION-MESSAGE.txt", activation.encode()),
                   ("WHATSAPP-MESSAGE.txt", share.encode()),
                   ("VALIDATION.txt", (ROOT / "docs" / "VALIDATION.md").read_bytes())]
    zip_bytes_path(team, team_items, c["date"])
    source = out / f"UX-Research-GitHub-Source-v{v}.zip"
    excluded = {"dist", ".git", "__pycache__", ".venv", "raw-research", "participant-data", "local-evaluations"}
    repo_items = []
    for p in sorted(ROOT.rglob("*")):
        rel = p.relative_to(ROOT)
        if any(part in excluded for part in rel.parts) or p.is_symlink() or not p.is_file():
            continue
        if p.name in {".DS_Store", "Thumbs.db"} or p.suffix == ".pyc":
            continue
        repo_items.append(("ux-research-skill/" + rel.as_posix(), p.read_bytes()))
    zip_bytes_path(source, repo_items, c["date"])
    artifacts = [native, folder_zip, gemini, txt, md, team, source]
    checksum = out / "CHECKSUMS.sha256"
    checksum.write_text("".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n" for p in artifacts), encoding="utf-8")
    return artifacts + [checksum]


if __name__ == "__main__":
    try:
        for artifact in build():
            print(f"{artifact.name}\t{artifact.stat().st_size:,} bytes")
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
