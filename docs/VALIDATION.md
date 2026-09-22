# Validation record — UX Research 0.1.0

**Date: 22 September 2026. Status: team pilot.**

The package was built and locally checked. No live installation into a separate ChatGPT, Gemini, Claude, or cloud account has been performed. No independent cross-model behavioural evaluation or research-speed comparison has been performed.

## Results actually obtained

| Check group | Result | What it establishes |
| :--- | :--- | :--- |
| Project-specific static validation | 23 / 23 passed | Known metadata, inventory, links, archive layouts, complete embedded content, version markers, and checksums match the release contract. |
| Automated unit tests | 22 / 22 passed | 14 deterministic evidence-counting tests and 8 package/build tests passed in the local Python environment. |
| Repeat-build determinism | Passed | Rebuilding identical canonical inputs produced byte-identical artifacts in the local environment. |
| Runtime inventory | 14 text files | One entrypoint, 11 reference modules, a start guide, and setup guidance; no executable runtime scripts. |
| Working templates | 12 present | The specified template sections are included. This is not proof of model output quality. |
| Calibration register | 21 records present | Material adaptations are documented and mapped to their source rationale. |
| Live model-evaluation scenarios | 24 specified; 0 executed | Prompts, expected behaviours, and critical failures are available for the team pilot. These are not model results. |
| Native ChatGPT Chat single-.skill import | Not run | Remains a release-validation item; the TXT fallback is a different usage route. |
| Other provider imports and model behaviour | Not run | Documentation alignment does not establish successful installation or execution. |

The deterministic fixture includes eight attendees, six known unaided task outcomes, one missing outcome, one unexposed participant, duplicate evidence, and assisted completion. The expected unaided failure result is **4/6**, with missingness and exposure reported separately. Tests exercise identity, duplication, conflicts, absent data, and invalid input. They do not prove an AI will extract or interpret those facts correctly.

## Reproduce the checks

From the repository root, with Python 3.10 or later:

```sh
python tools/build.py
python tools/validate.py
python -m unittest discover -s tests -v
```

The scripts use the standard library and do not call AI APIs. Build tools are outside native skill archives. The complete Chat edition embeds every runtime file, with rewritten internal links and an end-of-package marker. The folder .skill and folder ZIP are byte-identical; the Gemini ZIP has SKILL.md at its root. All output files have SHA-256 checksums in the generated release.

The executed local test log is in automated-test-results.txt. Machine-readable results are in validation-results.json. These records describe the delivered snapshot; rerun checks after any modification. The checker is project-specific, not the Agent Skills reference validator or a provider certification.

## Security and completeness limits

Archive checks cover safe paths, duplicate entries, no symbolic links, text-only runtime files, and equality to canonical source. A limited text-pattern scan found no matched private Notion URLs, workspace identifiers of the scanned forms, signed URLs, or credential patterns in the runtime. This is not a complete security, privacy, accessibility, intellectual-property, or legal audit.

No real participant records, private Notion exports, account credentials, or client research files are intentionally included. Examples and evaluation fixtures are synthetic. Provider guidance was checked against primary documentation on 22 September 2026 and can change.

## Required before broad team rollout

Use TEAM-PILOT.md to record real import and activation results for each surface. Test source access, task routing, correct denominators, unknown overlap, contradictions, missing files, privacy, injected commands, and H3 approval handling. Keep raw evaluations separate from public repository content. Never promote a static pass into a claim of live compatibility or universal reliability.
