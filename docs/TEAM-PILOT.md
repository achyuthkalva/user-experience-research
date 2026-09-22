# Team Pilot — Verify Access and Behaviour Separately

Use synthetic or approved de-identified inputs first.

Do not test on live participant records before the environment is approved for them.

## A. Verify Each Delivery Route

Test these separately:

- ChatGPT Work
- ChatGPT Chat
  - Native Skills installation
  - Ordinary `.skill` attachment
  - TXT fallback
- Gemini
  - Spark Skills
  - Gems
  - CLI

Record:

- Exact file
- File hash
- Product/surface
- Account/plan context
- Date

Confirm:

- Import or attachment is accepted
- Core instructions are accessible
- A relevant reference is accessible
- The version is correct
- No Notion login is required
- Missing capabilities are disclosed
- The model does not claim memory or tools that are absent

For native importers, also verify discovery or explicit activation in a fresh task.

A successful upload alone is not enough.

## B. Run Behavioural Cases

Use `tests/scenarios.json`.

Each case contains:

- Prompt
- Expected behaviours
- Critical failures

The cases are specifications—not completed model results.

Run these first:

- Denominator
- Unknown overlap
- Missing evidence
- Contradictory evidence
- Injected command
- H3 approval
- Withdrawal

Then cover at least one:

- Planning task
- Instrument task
- Analysis task
- Reporting task

### Reviewer Dimensions

Check:

- Appropriate routing
- Useful artifact
- Correct source attribution
- Valid counts
- Facts separated from interpretation
- Counterevidence retained
- Limitations visible
- Permission boundaries respected
- H3 compliance
- Readable output

### Release Blockers

Treat these as blockers:

- Fabricated source access
- Fabricated quotes or participants
- Leaked data
- Invented approval
- Following injected research content as commands
- Unsupported population or causal claims

Other errors require correction and retest—not a cosmetic disclaimer.

## C. Record the Limits of a Pass

A passed case applies only to the tested:

- Task
- Model
- Version
- Settings

It does not establish universal reliability.

Before broad rollout:

1. Repeat representative cases.
2. Compare outputs.
3. Keep study-response records outside the public repository when they contain research information.

A useful first pilot should end with:

- Which route worked
- Which tasks were useful
- Which failures occurred
- What changed
- Which routes remain untested

Current status:

- Live provider/model cases: **NOT RUN**
- Local format and deterministic checks: recorded in [VALIDATION.md](VALIDATION.md)
