# Validation Record — UX Research 0.1.0

Date: 22 September 2026  
Status: Team Pilot

The package was built and locally checked.

Not yet completed:

- Live installation in a separate ChatGPT, Gemini, Claude, or cloud account
- Independent cross-model behavioural evaluation
- Research-speed comparison

## Results Actually Obtained

| Check Group | Result | What It Establishes |
| :--- | :--- | :--- |
| Project-specific static validation | 23 / 23 passed | Metadata, inventory, links, archive layouts, embedded content, version markers, and checksums match the release contract |
| Automated unit tests | 22 / 22 passed | 14 deterministic evidence-counting tests and 8 package/build tests passed locally |
| Repeat-build determinism | Passed | Identical canonical inputs reproduced byte-identical artifacts locally |
| Runtime inventory | 14 text files | One entrypoint, 11 reference modules, a start guide, and setup guidance |
| Working templates | 12 present | Required template sections are included |
| Calibration register | 21 records present | Material adaptations are documented and source-mapped |
| Live model-evaluation scenarios | 24 specified · 0 executed | Test specifications exist; these are not model results |
| Native ChatGPT Chat single-.skill import | Not run | Remains a live validation item |
| Other provider imports and model behaviour | Not run | Documentation alignment is not proof of successful execution |

### Deterministic Fixture

The fixture includes:

- 8 attendees
- 6 known unaided task outcomes
- 1 missing outcome
- 1 unexposed participant
- Duplicate evidence
- Assisted completion

Expected unaided failure result:

- **4 / 6**
- Missingness and exposure reported separately

The tests cover:

- Identity
- Duplication
- Conflicts
- Missing data
- Invalid input

They do not prove an AI will extract or interpret those facts correctly.

## Reproduce the Checks

Requirements:

- Python 3.10+
- Standard library only

Run:

```sh
python tools/build.py
python tools/validate.py
python -m unittest discover -s tests -v
```

The build verifies:

- Complete runtime embedding
- Internal link rewriting
- End-of-package marker
- Byte-identical folder `.skill` and folder ZIP
- Root-level `SKILL.md` in the Gemini ZIP
- SHA-256 checksums

Evidence records:

- `automated-test-results.txt`
- `validation-results.json`

Rerun validation after any modification.

> [!NOTE]
> The checker is project-specific. It is not the Agent Skills reference validator or a provider certification.

## Security and Completeness Limits

Archive checks cover:

- Safe paths
- Duplicate entries
- No symbolic links
- Text-only runtime files
- Equality to canonical source

A limited text-pattern scan found no matched:

- Private Notion URLs
- Workspace identifiers of the scanned forms
- Signed URLs
- Credential patterns in the runtime

This is not a complete security, privacy, accessibility, intellectual-property, or legal audit.

No real participant records, private Notion exports, account credentials, or client research files are intentionally included.

Examples and evaluation fixtures are synthetic.

Provider guidance was checked against primary documentation on 22 September 2026 and can change.

## Required Before Broad Team Rollout

Use [TEAM-PILOT.md](TEAM-PILOT.md).

Verify:

- Import and activation for each surface
- Source access
- Task routing
- Correct denominators
- Unknown overlap
- Contradictory evidence
- Missing files
- Privacy behaviour
- Injected commands
- H3 approval handling

Keep raw evaluations separate from the public repository.

Do not turn a static pass into a claim of universal compatibility or reliability.
