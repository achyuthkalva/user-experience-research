# Setup and Compatibility — Separate the Format From the Runtime

Version 0.1.0 · Team Pilot

Documentation checked: 2026-09-22.

Primary references E1–E6 and E11–E14 are listed in [references/10-sources.md](references/10-sources.md).

> [!IMPORTANT]
> No live installation or end-to-end model evaluation in another account has been completed for this release.

## Deliverables

| File | Contents | Intended Use |
| :--- | :--- | :--- |
| `ux-research-v0.1.0.skill` | ZIP with one top-level `ux-research/` folder | Compatible skill loaders or archive-capable sessions |
| `ux-research-v0.1.0.zip` | Same folder archive with a ZIP extension | Folder-based importers and inspection |
| `ux-research-gemini-v0.1.0.zip` | Same text files with `SKILL.md` at archive root | Gemini Spark's documented layout |
| `UX-Research-Chat-v0.1.0.txt` / `.md` | Complete flattened edition | Conversational use without archive extraction |
| `UX-Research-Team-Pack-v0.1.0.zip` | Skill, alternate ZIPs, TXT edition, start guide, activation message | WhatsApp or another approved sharing channel |
| `UX-Research-GitHub-Source-v0.1.0.zip` | Editable source, docs, builder, validation, tests | Repository maintenance |

The core skill contains only UTF-8 Markdown/text.

It includes no:

- Executable runtime scripts
- Telemetry
- Credentials
- Mandatory connectors
- Automatic network calls

Repository tools build and validate releases. Teammates do not need them to use the skill.

## ChatGPT Work Mode

Treat Work as a distinct execution environment.

- Access depends on the surface, plan, workspace, and authorised tools.
- Local file access is not the same as cloud Work access.
- A skill file cannot grant connector or desktop permissions.
- Source read access does not imply permission to publish or contact participants.

Use the native Skills upload/install route when the workspace exposes it.

Otherwise:

1. Provide the complete Chat edition or unpacked source.
2. Ask Work to inventory accessible files.
3. Use only authorised tools.
4. Check H3 status before implementation.

See E2–E3 in the source register.

## ChatGPT Chat Mode With One `.skill` File

Keep two situations separate.

### Native Installed Skill

- Use the actual Skills importer available to the account.
- Follow the importer's permissions and restrictions.
- Public documentation reviewed does not prove every Chat importer accepts this release's `.skill` extension.

See E2.

### Ordinary Chat Attachment

A `.skill` file is an archive, not plain prose.

Use it only when the session can:

- Accept the file
- Read or extract the archive
- Access the referenced resources

A successful attachment is not proof that the skill loaded correctly.

If the archive route fails:

- Use the complete TXT or Markdown edition.
- Treat that as a conversational fallback, not a native skill installation.

The exact single-`.skill` Chat path remains a live validation item.

### Chat Operating Rules

- Provide the immediate task and evidence.
- Work in clear stages.
- Carry a context capsule between sessions when needed.
- Do not assume cross-chat memory.
- If a large attachment is only partly read, narrow the batch and state the limit.

## Gemini

### Spark Skills

Use `ux-research-gemini-v0.1.0.zip`.

At the documentation check:

- Spark accepted `SKILL.md` or a ZIP with `SKILL.md` in the main folder.
- Eligibility depended on account/subscription.
- Work/school account availability differed.

Confirm current eligibility before use.

Do not move confidential research into a personal account to bypass organisational controls.

See E4.

### Gems

Where available:

1. Create a Gem with instructions.
2. Add the complete TXT edition as knowledge.
3. Use the activation message.
4. Keep evidence and approval rules active.

This is not the same feature as Spark Skills.

See E5.

### Gemini CLI

Treat Gemini CLI as a separate agent runtime.

- Inspect the downloaded source.
- Use the skill installation route documented for the installed CLI version.
- Verify discovery and reload behaviour there.

See E11–E12.

## Claude and Other Comparable Agents

Anthropic documents folder-based ZIP packaging for custom skills.

Use the supplied folder ZIP only where the target importer supports that structure.

For any Agent Skills-compatible runtime:

- Use the `ux-research/` directory containing `SKILL.md`.
- Confirm referenced Markdown files are accessible.
- Confirm actual tool permissions.

The open standard describes a directory contract—not identical execution across hosts.

See E1 and E13.

## Hosted, Cloud, and API Environments

There is no universal “cloud importer.”

A developer must explicitly provide:

- Instructions/resources
- Evidence access
- State handling
- Tool permissions
- Approval enforcement

Where possible, enforce consequential approvals in application logic rather than relying only on model instructions.

Keep research evidence separate from the distributable skill.

Pin the release version used for each study.

See E6.

## Verification Levels

- **Documentation-aligned**
  - Packaging or feature route matches reviewed primary documentation.

- **Locally checked**
  - Structure, links, content inclusion, archive safety, and deterministic fixtures pass repository checks.

- **Live import passed**
  - A named person records the date, product/surface, plan, file/hash, and successful import.

- **Behavioural evaluation passed**
  - Actual model outputs are reviewed for routing, source access, counts, uncertainty, gate compliance, and usefulness.

Only the first two levels apply to this release.

A smoke test is an initial check—not proof of reliable behaviour across tasks or models.
