# 05 — Prioritise transparently and keep decisions human-owned

**Source basis:** Prism 04, Steps 5–6 and H3; Playbook §2.4 and §7.4. This module preserves Prism's named scale while separating evidence strength and organisational decisions.

## Step 5 — Apply Prism's custom severity scale

Use this scale only when an issue or opportunity warrants it. Positive findings and contextual observations may be “not applicable.” Missing information may require “not yet rated.” These are non-rating states, not additional levels.

| Rating | Original label | Criteria to apply and justify |
| :--- | :--- | :--- |
| 1 | Good To Know | Minor challenge; goal remains achievable; few participants affected in the available evidence |
| 2 | Table Stakes | Minor confusion/friction; a meaningful part of the study sample affected |
| 3 | Appreciable | Significant confusion or loss of the direct path; improvement could help traction |
| 4 | Important | Direct impact on the user outcome that warrants attention |
| 5 | Absolutely Important | Significant outcome impact plus a supported competitive-differentiation case |

These labels and thresholds come from Prism, not a universally accepted UX scale. “Meaningful part” needs contextual judgement, not an invented numerical cutoff. Without business or competitive evidence, do not infer a 5 solely from frequency. Record why a rating fits, what remains uncertain, and what evidence could change it. A severe rare issue can matter; do not mechanically downgrade it because only one person encountered it.

For each issue, separately capture:

- **Impact/severity:** effect on the user goal and context, with the Prism rationale.
- **Observed reach:** X/N with the correct unit, exposure, missingness, and subgroup limits.
- **Evidence strength:** what kind of claim is supported and how uncertain the interpretation is.
- **Business relevance:** verified goal connection or explicit assumption; no invented revenue impact.
- **Delivery considerations:** effort, dependencies, timing, accessibility, and capacity when known.
- **Priority:** proposed action order and trade-offs, awaiting the decision owner.

Do not collapse these into an unexplained weighted score. Cost calculations must show units, source inputs, assumptions, uncertainty, and sensitivity. They are not causal proof that a design change will produce savings.

## H3 — Stop before treating a proposed order as approved

Present the evidence, provisional severity order, known trade-offs, and proposed sequence for review. Ask the decision owner to approve or revise that specific sequence. Without that approval, deliver the provisional assessment and stop the transition into an approved action plan.

Recommendation options may be drafted independently when requested, but label them “options for review; not an approved sequence.” Do not assign commitments, deadlines, implementation status, or approved priorities without evidence of authority. Do not infer approval from “use your judgement,” a previous setup approval, or an AI-generated context field. Request explicit approval of the order shown, or leave it provisional.

Record approval statement, decision owner, available date/message reference, scope, and any changes. Do not invent a timestamp. Revisit approval when new evidence materially changes the sequence.

## Step 6 — Recommend against the insight, not each isolated observation

After the priority gate is resolved, develop one recommendation set per supported insight. Multiple actions may address one underlying issue. For each action specify: the intended outcome, link to the insight and evidence, proposed intervention or next learning step, trade-offs, dependencies, validation method, and owner/date only when supplied or explicitly assigned.

Keep design proposals separate from evidence. “Add a preview” is a candidate solution, not a research finding. When the explanation is uncertain, a prototype or targeted follow-up may be more defensible than an implementation commitment.

Address the root issue where supported, consider alternate solutions and affected secondary users, and define how success or failure would be detected. Do not claim a recommendation has been tested before evidence exists. Where maintaining current behaviour is justified, say so; do not invent work to fill a template.

**Output:** T9 in 08 and a short status line: provisional / approved for stated scope / blocked. The report must preserve this status.
