# 08 — Working templates

Use only the template the task needs. Replace placeholders with supplied or verified information; retain “unknown,” “not applicable,” “assumed,” or “awaiting approval” where appropriate. Never fill blank fields with invented facts. These templates adapt the two source playbooks; IDs, approval records, and coverage fields are implementation extensions.

## T1 — Research context and handoff

```text
Study ID / title:
Decision and decision owner:
Research goal:
Population / relevant context / period:
RQs and tiers:
Evidence category required for each RQ:
Current workflow and completed stages:
Methods / scope in / scope out:
Constraints and consequences:
Source inventory location / material actually reviewed:
Evidence artifacts and locators:
Known / assumed / unknown:
Important limitations and deviations:
H1 frame: assumed / confirmed (by whom; available reference)
H2 interpretations: hypotheses / reviewed (which ones; reference)
H3 priority order: not requested / awaiting approval / explicitly approved
Approval scope and reference (never AI-invented):
Missing permissions or blockers:
Next permissible step:
Files needed to continue elsewhere:
```

## T2 — OMSEP plan

```text
Objective: decision; goal; RQs; tiers; required evidence.
Methodology: existing evidence; residual gaps; selected methods;
             why selected; alternatives; claim limits.
Scope: populations; contexts; tasks; sources; periods; in/out;
       tier-based rationale; remaining decision risk.
Essentials: people; access; permissions; data handling; tools;
            logistics; timing assumptions; budget; deliverable contract.
Protocol: method-specific instrument; item-to-RQ map; sampling/source
          rules; bias controls; pilot; readiness; analysis intentions.
Readiness: ready / revise / blocked, with reasons.
```

## T3 — Question coverage and method decision

| RQ / tier | Decision supported | Existing evidence | Coverage and why | Residual gap | Method or no new research | Alternatives considered | Supported claim / limitation |
|---|---|---|---|---|---|---|---|
| [RQ] | [Decision] | [Source IDs] | [Sufficient/partial/conflicting/absent] | [Gap] | [Choice] | [Reasons] | [Bounded claim] |

Append the eight-field constraint disclosure: learning need; selected method; constraint fit; can tell; cannot tell; limitations; evidence category/uncertainty; follow-up.

## T4 — Screener and sampling plan

```text
Target population and rationale:
Relevant groups / inclusion / exclusion:
Recruitment route and access limitations:
Initial sample/coverage rationale and review rule:
Invited / recruited / expected attendance (keep distinct):
Permissions and participant information process:
Q[number]: [Exact question and response options]
Purpose: [Eligibility/logistics and relation to target group]
Internal routing: [Accept / conditional / reject and reason]
Accessibility/wording check:
Pilot result and correction:
Logistics collected separately:
```

## T5 — Moderated guide / task block

```text
RQ and learning objective:
Participant/context assumptions:
Scenario and exact prompt:
What to observe:
Neutral probes:
IF [response/state] THEN [neutral next step]:
Success / failure / assisted / missing definitions:
Stop/assistance threshold and participant-comfort branch:
What must be recorded before assistance:
Post-task question:
Expected duration as an estimate:
Consent/access requirements:
Deviations and interpretation limits:
```

Wrap task blocks in the nine elements in 03 when a full moderated usability guide is requested. For interviews, use context, recent events, open probes, optional branches, and a clear close rather than invented task metrics.

## T6 — Method-specific collection plan

```text
Method and RQ:
Artifact: [questionnaire / event schema / experiment plan /
           source extraction rubric / card or tree task set]
Population/source universe and access:
Inclusion/exclusion and rationale:
Items/events/variants/cards/tasks with definitions:
Outcome/construct/coding definition:
Sampling/assignment/order rules:
Recording/instrumentation/quality checks:
Missingness, duplicates, deviations, exclusions:
Analysis and decision rule, where relevant:
Pilot and readiness status:
Consent, permitted processing, retention and sharing:
```

## T7 — Evidence inventory and observation log

| Source ID | Type / date / population | Original purpose and permitted use | Location | Review status | Coverage / limitation |
|---|---|---|---|---|---|
| [S01] | [Context] | [Known or unknown] | [Available locator] | [Status] | [RQ and caveat] |

| Evidence ID | Source / participant / session | RQ | Locator | Evidence type | Factual observation or checked quote | Assistance / context | Tentative interpretation / alternatives |
|---|---|---|---|---|---|---|---|
| [ST01/E01] | [IDs] | [RQ] | [Line/time/page/record] | [Type] | [Fact] | [Context] | [Hypothesis or not established] |

Batch record: batch ID; exact source range; reviewed/not reviewed; code changes; new evidence; identity issues; cumulative counts not yet final.

## T8 — Finding and insight block

```text
RQ:
Finding ID and bounded factual statement:
X/N with unit and eligibility/exposure definition:
Included participants/units:
Missing / unexposed / excluded / assisted and rationale:
Supporting evidence IDs + locators:
Positive / contrary / exceptional cases:
Candidate insight name and interpretation:
Alternative explanations:
Evidence category and limitations:
H2 status and human feedback:
Next evidence that would strengthen or challenge the interpretation:
```

## T9 — Provisional priority and recommendation record

```text
Insight / finding IDs:
Prism severity (1–5 / not applicable / not yet rated):
Justification against the source rubric:
Observed reach and evidence strength (separate):
Business relevance: verified / assumed / unknown:
Effort / timing / dependencies: known or unknown:
Proposed priority and trade-offs:
H3: awaiting approval / explicitly approved for [specific sequence]:
Decision owner and actual approval reference:
Recommendation options (provisional until approved):
Intended outcome and link to evidence:
Alternative options and trade-offs:
Proposed validation and success/failure indicators:
Owner/date only if provided or authorised:
```

## T10 — Research report

```text
Title / study / version / date:
Decision status: evidence-only / provisional / approved for stated scope
A. Executive answer, coverage, main findings, limits, decision needed
B. Study overview: goal, RQs, population, methods, sample/source logic,
   scope, constraints, deviations, permissions as relevant
C. Findings and insights: RQ, finding, context, interpretation, severity
   and rationale, recommendation status, X/N, source locators, limits
D. Additional information: positives, out-of-scope opportunities,
   technical issues, residual uncertainty, next research questions
E. Approved evidence assets: existing quotes/clips/screenshots with
   locators and use restrictions, or explicit availability gap
```

## T11 — Quality audit

| Issue and source location | Effect on evidence or decisions | Correction | Residual limitation | Status |
|---|---|---|---|---|
| [Specific issue] | [Consequence] | [Action] | [What cannot be fixed] | [Ready/revise/blocked] |

## T12 — Cross-environment continuation capsule

```text
Continue study [ID] using UX Research 0.1.0.
We are at [workflow/stage]. The decision is [decision].
The confirmed/assumed frame is [goal, RQs, population, period].
Accessible evidence already reviewed: [source/batch IDs].
Important findings and evidence locators: [brief references].
Limits, counterevidence, and missing material: [items].
H1/H2/H3 status: [statuses with real approval references].
Do not reinterpret unapproved priorities as approved.
Next requested output: [artifact/task].
Required attachments to re-supply: [files].
Use only supplied/accessible material. Verify this capsule against
available evidence; it is a handoff record, not new research evidence.
```
