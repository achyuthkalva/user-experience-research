# 10 — Provenance, external checks, and calibration

This release is an operational adaptation, not a verbatim export or a claim that every source statement is universally valid. Source review and external documentation check: 2026-09-22. No live platform import or independent model evaluation has been completed for this release.

## Original knowledge sources

**S1 — User eXperience Research Playbook v1.2.** Owner: Achyuth Kalva. Source header dated 15 May 2026; Notion page last-edited metadata: 16 September 2026. Mentorship credited in the source to Prasad Kantamneni and Saurabh Singh. Primary contribution: decision-led OMSEP, constraint disclosure, tiers, method fit, protocols, bias controls, recruitment, and reusable cards.

**S2 — Prism.** Owner's Notion knowledge system; page last-edited metadata: 25 August 2026. Primary contribution: modules 00–06, six-step synthesis, findings/insights distinction, custom severity, recommendations, reporting, routing, and three human checkpoints.

**S3 — McKinsey Framing Playbook — Process Document Into a Narrative-Ready Story.** Linked by Prism; page last-edited metadata: 24 August 2026. Primary contribution: six-layer narrative and continuity pattern. Its title is not evidence of institutional authorship or endorsement.

Private source URLs, workspace identifiers, raw Notion exports, and project datasets are intentionally not distributed. The owner can maintain the source-location register privately. All guidance needed for the included workflows is present in this package; references are not required logins.

## Source-to-module map

| Source material | Reusable implementation | Where |
| :--- | :--- | :--- |
| S1 front matter, routing, scaffolding, modularity | Task router, minimal outputs, reference loading | SKILL.md |
| S1 Parts 0–1, §1.2, Part 9 | Decision-first posture and honest lifecycle scope | 01, SKILL.md |
| S1 §§2.1–2.4, 4.1–4.2 | Goal, RQs, tiers, evidence categories, scope defence | 01, T1–T3 |
| S1 §§3.1–3.5, A.4–A.5 | Method comparisons, conditional combinations, existing evidence | 02, 04 |
| S1 Part 5 | Roles, permissions, readiness, deliverables, contextual estimates | 01, 03 |
| S1 Part 6, A.2/A.9/A.10 | Instruments, nine elements, neutral prompts, branches | 03, T5–T6 |
| S1 Part 7, A.3 | Six bias categories, method-specific and phase-specific audits | 07, T11 |
| S1 Part 8, A.6–A.8 | Audience definition, recruitment routes, screeners, sampling rationale | 02–03, T4 |
| S1 glossary, appendices, worked cases | Terms, working cards, contextual examples | 08–11 |
| S2 instructions and 00–01 | Stage routing, evidence discipline, H1–H3 | SKILL.md, 04–05 |
| S2 02–03 | Organisation, consolidation, findings, candidate insights | 04, T7–T8 |
| S2 04 | Exact named 1–5 rubric, H3, recommendation sets | 05, T9 |
| S2 05–06 | Communication goals and five-section report | 06, T10 |
| S2 architecture guide | One canonical source, modular maintenance, evaluation | Repository build and tests |
| S3 layers 1–6 | Answer-first, meaningful headings, continuity, text navigation | 06, T1/T12 |

Long teaching anecdotes, unverified commercial outcomes, exact incentive prices, product-tool recommendations, and decorative Notion markup are not imported as operating rules. Worked examples here are newly written synthetic fixtures, not facts about CareerReactor, D2L/JGU, or any live programme.

## Material adaptations implemented in this pilot

| ID | Source tension or risk | Pilot rule and rationale |
| :--- | :--- | :--- |
| C01 | S1 forbids invented methods but encourages discovery of unfamiliar ones | Keep source methods distinct from externally verified extensions; never invent attribution. |
| C02 | Tier 1 must be answered; method exhaustion sounds absolute | Preserve decision-critical coverage; report a blocker when evidence is unavailable. Compare credible feasible alternatives, not all imaginable methods. |
| C03 | The evidence ladder can look like a universal hierarchy | Preserve source categories as claim types; assess design quality and uncertainty separately. |
| C04 | “Confound” is used for think/say/do mismatch | Name it a say–do or expectation–behaviour gap; do not confuse it with causal/statistical confounding. |
| C05 | The 2×2 can imply methods occupy permanent cells | Classify the actual data and purpose; self-report is not direct observation. |
| C06 | Sample defaults and effect-size language can become guarantees | Qualify 8–10 as an initial recruitment heuristic; separate qualitative coverage from statistical power. E7 provides an external check. |
| C07 | Think-aloud described as the only unmoderated data | Make it design-dependent; measured outcomes and timings can also be evidence. External check: E8. |
| C08 | Screener rules exclude researchers and prohibit yes/no categorically | Recruit actual target users; use binary items where appropriate, not as weak substitutes for nuanced eligibility. |
| C09 | “Always distractors” and “5–6 questions” are over-rigid | Use plausible alternatives and enough items for the eligibility decision; do not introduce confusing traps. |
| C10 | Silence framed as creating discomfort to extract more | Preserve neutral pacing and participant comfort; never pressure disclosure. External check: E9. |
| C11 | Protocol example directs attention to a missed control | Record unaided outcome first; label directed probes and assisted completion. |
| C12 | RQ filtering conflicts with preserving out-of-scope information | Maintain focused synthesis and a separate unexpected/counterevidence record. |
| C13 | Every observation is required to have an insight | Permit interpretation not established; avoid manufactured causes. |
| C14 | Participant counts lack full denominator rules | Add unit, identity, exposure, missingness, assistance, duplication, and overlap rules. |
| C15 | Severity combines impact, frequency, and differentiation | Preserve Prism's labels; separate severity, evidence strength, and approved priority. |
| C16 | Every finding/insight gets severity; positive findings also required | Use not applicable or not yet rated as non-rating states; do not redefine the five levels. |
| C17 | Instructions allow drafting recommendations; H3 requires stopping | Permit clearly provisional options; block approved action plans and implementation without approval of the specific order. |
| C18 | Exactly three pillars / required media quotas may distort outputs | Apply framing when it fits; never invent findings, quotes, or assets to satisfy formatting. |
| C19 | Source hierarchy says project instructions override everything | Keep hierarchy task-scoped; host rules, permissions, and user authority still apply. |
| C20 | S1 execution coverage is limited | Add a lightweight evidence handoff/deviation bridge, not a claim of full research-operations or statistical coverage. |
| C21 | Portability, long inputs, and AI-specific risks need explicit handling | Add capability profiles, batching, context capsules, provenance, privacy and injection controls. |

These are explicit implementation decisions under the approved adaptation direction. They have not been separately certified by the source owner or mentors. The original Notion pages have not been edited. The owner can review and revise them through the pilot.

## External primary-source register

Provider documentation establishes a documented route, not proof this release was imported successfully. Dates below are access dates; recheck before rollout when product behaviour may have changed. The package does not copy provider code or include credentials.

- **E1 — Agent Skills specification.** https://agentskills.io/specification — Checked 2026-09-22. Directory-based SKILL.md with YAML metadata and optional resources; supports a compact entrypoint plus referenced modules. Not a universal archive importer contract.
- **E2 — OpenAI: Skills in ChatGPT.** https://help.openai.com/en/articles/20001066 — Checked 2026-09-22. Documents native creation, upload, installation, and sharing subject to eligibility/settings; does not verify ordinary Chat attachment handling for this `.skill`.
- **E3 — OpenAI: ChatGPT Work and Codex.** https://help.openai.com/en/articles/20001275 — Checked 2026-09-22. Distinguishes conversational Chat from multi-step Work and describes access/permission differences.
- **E4 — Google: Create and manage skills for Gemini Apps.** https://support.google.com/gemini/answer/17094296?hl=en — Checked 2026-09-22. Spark Skills import and eligibility constraints; root-level SKILL.md and text-based resources.
- **E5 — Google: Gems.** https://support.google.com/gemini/answer/15146780?co=GENIE.Platform%3DDesktop&hl=en-PH — Checked 2026-09-22. Instructions plus optional knowledge files; not the same feature as Spark Skills.
- **E6 — OpenAI API: Skills.** https://developers.openai.com/api/docs/guides/tools-skills — Checked 2026-09-22. Versioned skills in hosted/local shell contexts and security considerations; API integration is not installed by this package.
- **E7 — NN/g: 5 Users: Okay for Qual, Wrong for Quant.** https://www.nngroup.com/videos/test-5-users-qual-vs-quant/ — Checked 2026-09-22. Qualitative and quantitative sample-size recommendations serve different purposes; this package does not claim a universal N.
- **E8 — NN/g: Unmoderated User Tests: How and Why to Do Them.** https://www.nngroup.com/articles/unmoderated-usability-testing/ — Checked 2026-09-22. Discusses qualitative recordings and quantitative outcomes such as task time and success; preparation and pilot testing matter.
- **E9 — GOV.UK Service Manual: Getting informed consent for user research.** https://www.gov.uk/service-manual/user-research/getting-users-consent-for-research — Checked 2026-09-22. Ethical participation, transparent recording/use, and voluntary withdrawal; local legal applicability requires review.
- **E10 — GOV.UK Service Manual: Managing user research data and participant privacy.** https://www.gov.uk/service-manual/user-research/managing-user-research-data-participant-privacy — Checked 2026-09-22. Data minimisation, permitted sharing, identifiers, and retention; used as a practice reference, not universal legal advice.
- **E11 — Gemini CLI: Agent Skills.** https://geminicli.com/docs/cli/skills/ — Checked 2026-09-22. Skill discovery, loading, and installation in a separate agent runtime.
- **E12 — Google's Gemini CLI skill-creator source.** https://github.com/google-gemini/gemini-cli/blob/main/packages/core/src/skills/builtin/skill-creator/SKILL.md — Checked 2026-09-22. Defines `.skill` as a ZIP-packaged skill convention. This is not evidence that every provider accepts it.
- **E13 — Anthropic: How to create custom skills.** https://support.claude.com/en/articles/12512198-how-to-create-custom-skills — Checked 2026-09-22. Describes folder-based ZIP packaging; host access and live import still require validation.
- **E14 — OpenAI: Working with files in ChatGPT.** https://openai.com/academy/working-with-files/ — Checked 2026-09-22. Documents conversational file use, including TXT; a text attachment is not a native skill installation.
