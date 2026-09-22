# Maintain One Canonical Workflow

1. Edit `skills/ux-research/` for workflow changes.
   - Keep the core under 500 lines.
   - Route detail to focused references.
   - Avoid independently maintained platform variants.

2. For a source change:
   - Update the provenance/source map in reference 10.
   - Record whether the rule was retained, qualified, or added.
   - Do not silently overwrite the original methodology.

3. Update release metadata together:
   - `release.json`
   - Skill version
   - Start guide
   - Setup guide
   - Templates
   - README
   - Changelog

4. Rebuild and rerun all checks.
   - Inspect the Chat edition.
   - Inspect both ZIP layouts.
   - Keep provider/API guidance explicitly dated.

5. Repeat relevant model-evaluation cases after changes to:
   - Routing
   - Evidence handling
   - Approval logic

6. Create a tagged release only after reviewing:
   - Content
   - Distribution terms
   - Compatibility claims

Do not label an untested adapter as verified.

The builder uses:

- Standard-library Python
- Fixed ZIP metadata
- Deterministic inputs

Build and validation scripts are maintenance tools—not runtime dependencies.

## What to Record for a Model Run

Capture:

- Release version
- Artifact hash
- Provider / product / surface
- Reported model
- Relevant plan and settings
- Date
- Task ID
- Input fixture version
- Actual output location
- Reviewer
- Per-criterion outcome
- Critical failures
- Corrective change
- Retest reference

Do not treat these as independent behavioural evaluation:

- Source-document review
- Successful file upload
- A model claiming it loaded the skill
- Passing deterministic Python tests
