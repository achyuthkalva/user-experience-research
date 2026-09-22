# 02 — Choose methods by the question and its constraints

**Source basis:** Playbook v1.2, §2.3–2.4, §3.1–3.5, Appendix A.4–A.5. These method cards are paraphrased operational guidance, not universal cost, sample, or timing claims.

## Select the evidence, then the method

| Method | Best-fit uncertainty | Minimum setup / useful output | Key limitation and sensible pairing |
|---|---|---|---|
| Interviews | Accounts of needs, motivations, work context, past experiences | Relevant participants; neutral guide; contextual accounts | Recall and social-desirability effects; pair important claims with observation or records |
| Contextual inquiry | How work happens in its real setting | Access, permission, observation focus, contextual notes | Access and observer effects; contextual findings may not transfer to other settings |
| Diary study | Experiences and change over time | Participant commitment, manageable prompts, planned duration and check-ins | Missing entries and selective reporting; analyse participation and context |
| Moderated usability | Where and how a task/experience breaks down | Realistic tasks; relevant participants; observable product or prototype; assistance rules | Small selected samples and researcher effects; does not automatically size prevalence |
| Unmoderated usability | Independent task performance across participants | Understandable tasks; adequate prototype instrumentation; pilot; quality checks | Limited probing; record task outcomes, clicks, timings or narration appropriate to the design |
| Remote panel testing | Fast access to a broad recruitable audience | Panel fit, screener, task pilot, budget | Panel may not match specialised users; delivery speed and quality are not guaranteed |
| Survey | Defined constructs, attitudes, reported behaviour, estimates within a sampling design | Questionnaire, sampling frame, response plan, pilot, analysis plan | Selection/nonresponse and wording effects; larger N does not eliminate bias |
| Card sorting | How people group and label information | Card set, open/closed/hybrid design, target audience | Categorisation is not demonstrated findability or overall usability |
| Tree testing | Findability within a proposed hierarchy | Text tree, realistic tasks, success/path definitions | Does not measure the full interface; pair with usability when visual context matters |
| Session analysis | Recorded sequences, errors, use patterns | Valid events or recordings; segment/time definitions; appropriate permissions | Logs show recorded activity, not the full context or proven intent |
| Funnel analysis | Where measured progression changes or stops | Defined entry population, ordered events, time window, conversion denominator | Missing events and wrong sequences can mislead; pair with contextual explanation |
| Click/scroll maps | Page-level interaction or exposure | Sufficient relevant events; device and page-state segmentation | Aggregates conceal context; neither a click nor a scroll proves understanding |
| A/B or controlled comparison | Effect of a defined difference on specified outcomes | Allocation/design, metrics, power/precision plan, duration, stopping rule | Confounding, multiple comparisons, underpower, and early stopping undermine claims |
| Heuristic evaluation | Expert-identified potential usability issues | Stated heuristics, evaluator expertise, task context | Expert assessment is not evidence of actual user experience |
| Cognitive walkthrough | Assumptions about first-use task reasoning | Defined user knowledge, goal and action sequence | Depends on evaluator assumptions; validate important risks with users |
| Review mining | Unprompted concerns in available feedback | Source strategy, inclusion rules, deduplication, coding | Self-selection and extreme views; absence of complaints is not absence of problems |
| Support-ticket analysis | Problems reported to support and operational load | Ticket taxonomy, period, deduplication, unit definition | Misses silent failures; multiple tickets may represent one person or incident |
| Desk/literature review | Existing knowledge and context | Credible, dated, relevant sources and an extraction log | Population, product, geography, and time may not match |
| Stakeholder/proxy interviews | Goals, history, constraints, operational understanding | Relevant roles, explicit perspective, source labels | Stakeholders/proxies do not substitute for end users unless they are actual target users |
| Competitor review | Comparable approaches and hypotheses | Explicit comparison criteria, dated artifacts | Do not infer user needs, effectiveness, or commercial success from a competitor feature |

The source's 2×2 is a navigation aid. Many methods can produce both qualitative and quantitative data. Distinguish observed activity, self-reported behaviour, and inferred intent regardless of method name.

## Compare a small, credible set of alternatives

For each RQ, write: required claim → available evidence → gap → candidate methods → selected option → rejected feasible alternatives → limitations. Compare the few relevant alternatives; do not make a performative list of every method.

Choose the strongest feasible evidence, not the most elaborate study. An existing traceable record can be more useful than fresh weak interviews. A fresh interview can be essential when old records do not explain the current context.

### Typical branches

- No direct users: inspect existing first-party evidence; then relevant secondary evidence or expert/proxy work. Label the distinction. Do not recruit synthetic users.
- No analytics: do not plan a funnel audit as though instrumentation exists. Assess usable records or a different method; disclose that sizing may remain unanswered.
- One week: first check source access and recruitment feasibility. Use existing evidence to locate gaps; commission only the work that can credibly finish. Do not promise same-day panel results.
- High-stakes decision: strengthen design and triangulation; narrow or defer unsupported decisions. Do not compensate for weak evidence with persuasive presentation.
- Comparing subgroups: define the subgroup question and coverage before pooling; do not present two interviews per group as a statistically supported difference.

## Sampling is a design decision, not a magic number

The source's 8–10 recruits per relevant group is a practical qualitative planning starting point, including potential no-shows, not a guarantee of saturation. Distinguish invited, recruited, attended, included, exposed, and completed counts. Set an initial coverage goal and a stopping/review rule appropriate to diversity, study scope, evidence quality, and emerging gaps.

For quantitative estimates or experiments, establish the estimand/metric, population, baseline or variability, required precision or minimum detectable effect, design, error tolerance, and appropriate analysis. Do not output a sample-size calculation without its inputs and assumptions. Use a qualified analyst for statistical work beyond the available evidence and validated tooling. Qualitative recurrence is not an effect-size or power calculation. See external check E7 in 10.

## Discover unfamiliar methods without pretending they came from the playbook

With browsing available: define the method from primary guidance; inspect assumptions and evidence types; compare cost/access needs; explain fit; label the recommendation an external extension. Without browsing: identify what needs verification and restrict claims. Do not invent frameworks or attribute new guidance to the source owner.
