# 09 — Synthetic examples and setup smoke tests

Every example below is fictional and for training or evaluation only. Do not reuse its participants, counts, quotes, or conclusions as evidence in a real study.

## Example A — Existing evidence comes before new recruitment

**Synthetic input:** A team must decide which onboarding step to investigate. It has a current, validated funnel and five selected support tickets, but no recordings. The funnel identifies a measured drop at identity verification; tickets mention documentation uncertainty.

**Expected output:** The funnel locates a measured problem in its defined population. Selected tickets provide possible explanations, not prevalence or proof of causation. First check event quality, ticket selection and duplication, and whether the populations/periods match. Propose targeted contextual research only for the explanation still needed. Do not automatically recommend a broad survey or call the five tickets five unique users.

## Example B — Correct the denominator and preserve assistance

**Synthetic fixture, study DEMO-01, task FIND:** Eight participants attended. P01–P06 were exposed with usable outcomes. P07 was exposed but the outcome is missing. P08 did not reach the task. P01–P04 failed unaided; P05–P06 completed unaided. P02 later completed after a rescue prompt. A duplicate note repeats P01's same failure.

**Expected finding:** “Four of six participants with known task outcomes did not complete unaided (P01–P04). One further exposed participant has a missing outcome, and one attendee was not exposed. P02 later completed with assistance.”

**Do not say:** “Five failures” because a duplicate note exists; “four of eight failed” without explaining missing/exposure; “P02 succeeded unaided”; or “67% of all customers fail.”

**Candidate interpretation:** Findability or task comprehension may be involved. Evidence is insufficient to choose between these explanations from outcomes alone. H2 remains a hypothesis; severity is not automatically 5. Do not invent a label-clarity root cause, competitor data, or a revenue effect.

## Example C — Unknown overlap stays unknown

**Synthetic input:** “Eight participants took part. Five could not find the submit control and three abandoned. We do not know which participants were in both groups.”

**Expected output:** Preserve the two supplied counts, request identifiers or overlap information if a combined count is needed, and do not claim eight distinct affected participants. Do not claim that all abandonment was caused by findability. The union could be five to eight people under the stated total, but the actual count is unknown.

## Example D — Respect the priority gate

**Synthetic input:** The assistant has proposed order A → B → C. No person has approved that sequence. The user says, “Continue with the report.”

**Expected output:** Produce a findings/provisional-priority report with the order clearly awaiting approval. Do not call it an approved action plan, assign implementation commitments, or treat the generic instruction as H3 approval. A later explicit “I approve A → B → C for this study” resolves the gate for that sequence only.

## Example E — Do not lose a positive or contrary case

**Synthetic input:** Several people requested onboarding guidance, while an experienced subgroup completed the workflow and found extra prompts distracting.

**Expected output:** Preserve subgroup context and both patterns. Consider a conditional guidance hypothesis rather than universally adding mandatory steps. Do not bury the experienced subgroup to make the headline simpler.

## Setup smoke test

After loading the skill, ask:

> Check setup for UX Research. State the version, available modules, whether you are using a native skill or conversational attachment, and any material access limits. Then apply the fictional task-outcome fixture in Example B. Give the bounded finding, missingness, one tentative interpretation, and the approval status. Do not create an approved action plan.

A satisfactory response accesses the appropriate instructions, reports the expected 4/6 known outcomes with the two coverage caveats, keeps assistance separate, and leaves H3 unapproved. A fluent answer alone does not prove full installation or reliable use of every module.
