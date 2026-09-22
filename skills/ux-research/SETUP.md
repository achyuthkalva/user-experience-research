# Setup and compatibility — separate the format from the runtime

Version 0.1.0, team pilot. Documentation checked 2026-09-22. Primary references E1–E6 and E11–E14 are listed in references/10-sources.md. **No live installation or end-to-end model evaluation in another account has been run for this release.**

## What the deliverables actually are

| File | Contents | Intended use |
| :--- | :--- | :--- |
| `ux-research-v0.1.0.skill` | ZIP archive with one top-level `ux-research/` folder | Single-file distribution to compatible skill loaders or archive-capable sessions |
| `ux-research-v0.1.0.zip` | The same folder archive under a ZIP extension | Folder-based importers and transparent inspection |
| `ux-research-gemini-v0.1.0.zip` | Same text files with SKILL.md at archive root | Gemini Spark's documented layout |
| `UX-Research-Chat-v0.1.0.txt` / `.md` | Complete flattened edition generated from the same canonical files | Conversational use without archive extraction |
| `UX-Research-Team-Pack-v0.1.0.zip` | Skill, alternate import ZIPs, TXT edition, start guide and activation message | A single package to send through WhatsApp or another approved file-sharing channel |
| `UX-Research-GitHub-Source-v0.1.0.zip` | Editable source, docs, reproducible builder, validation code, test cases | Future repository maintenance; not an importer package |

The core skill contains only UTF-8 Markdown/text. It has no executable runtime scripts, telemetry, credentials, mandatory connectors, or automatic network calls. Repository tools build and validate releases; they are not needed by teammates using the skill.

## ChatGPT Work Mode

OpenAI describes Work as the multi-step agent experience and Chat as the conversational experience. Access and tools depend on the surface, plan, and workspace. Local file access is not equivalent to cloud Work access. See E3.

Use the native Skills upload/install route where your workspace exposes it; see E2. The exact importer must accept the supplied format. Otherwise provide Work with the complete Chat edition or unpacked source and ask it to use the relevant modules. This is task guidance, not a claimed native installation.

Use the Work/agent profile in SKILL.md. Let it inventory accessible files, plan necessary steps, and produce authorised artifacts. A file cannot grant permission to connectors or desktop data. Check H3 status before implementation. Do not confuse source read access with permission to publish or contact participants.

## ChatGPT Chat Mode with one `.skill` file

Two different situations must remain visible:

**Native installed skill:** eligible ChatGPT accounts can upload/install Skills using the Skills interface. Follow the actual importer and permissions. Public documentation reviewed does not establish that this release's `.skill` extension is accepted by every Chat importer. See E2.

**Ordinary chat attachment:** a single `.skill` is an archive, not necessarily readable prose to the host. Attach it only when your session accepts it, then request the activation/access check. The assistant needs a supported way to read or extract the archive and its references. Successfully naming the file is not proof the contents were loaded.

If the file is rejected or its resources cannot be read, use the complete TXT or Markdown edition. ChatGPT documents TXT attachment workflows (E14). This fallback preserves the content but **does not satisfy native `.skill` import** and must not be labelled as doing so. The exact single-`.skill` Chat path remains a live validation item.

Use the Chat profile: provide the immediate task and evidence, work in appropriate stages, and carry a context capsule when switching sessions. Do not assume selective reference loading or cross-chat memory. If a large attachment is only partly read, use a narrower task/batch and state the limit.

## Gemini

**Spark Skills:** Google's documented import accepts SKILL.md or a ZIP with SKILL.md in its main folder and plain-text resources. At the documentation check, Skills were Spark-only, required an eligible personal account/subscription, and were not available to work/school accounts. Confirm current eligibility; do not move confidential research into a personal account to bypass controls. Use the dedicated Gemini ZIP and run the smoke test. See E4.

**Gems / conversational adaptation:** where available, create a Gem with instructions and add the complete TXT edition as knowledge. This uses a different feature from native Spark Skills. Use the activation message as a starting instruction and require the evidence/approval checks in the core. See E5. Do not promise that a knowledge attachment is always loaded in full.

**Gemini CLI:** a separate agent surface with skill installation and resource handling. Its official skill-creator documents `.skill` ZIP packaging; its instructions are not proof of ChatGPT compatibility. Inspect the downloaded source, use the local skill installation route documented for your CLI version, and verify discovery/reloading there. See E11–E12.

## Claude and other comparable agents

Anthropic documents folder-based ZIP packaging for custom skills. The folder ZIP supplied here targets that structural pattern; account settings, importer changes, and actual behaviour still need checking. See E13.

For any Agent Skills-compatible runtime, use the `ux-research/` directory containing SKILL.md. Check support for referenced Markdown files and actual tools. The open standard describes the directory contract, not identical execution across hosts. See E1.

## Hosted / cloud / API environments

The cloud is not one importer. A developer must load the appropriate instructions/resources, provide evidence access, keep state, and implement tool permissions. For example, OpenAI's API documents versioned skill bundles and attaching them to hosted shell environments; see E6. This repository does not create an API deployment, backend, secret store, or provider subscription.

Enforce consequential approvals in application logic where possible rather than relying solely on model instructions. Keep research evidence separate from the distributable skill. Pin a release and record what version was used for a study.

## Verification levels

**Documentation-aligned:** packaging or feature route matches reviewed primary documentation.

**Locally checked:** release structure, links, content inclusion, archive safety, and deterministic test fixtures checked by repository tools.

**Live import passed:** a named person records date, product/surface, plan, file/hash, and successful import in the target environment.

**Behavioural evaluation passed:** actual outputs from the test cases are reviewed for routing, source access, counts, uncertainty, gate compliance, and usefulness.

Only the first two levels apply at this release. A smoke-test answer is an initial check, not a guarantee of dependable performance across tasks or models.
