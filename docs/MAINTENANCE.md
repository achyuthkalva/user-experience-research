# Maintain one canonical workflow

1. Edit `skills/ux-research/` for workflow changes. Keep the core under 500 lines and route detail to focused references. Avoid parallel independently edited platform versions.
2. For a source change, update the provenance/source map in reference 10 and explain whether the rule was retained, qualified, or added. Do not silently overwrite the original methodology.
3. Update `release.json`, the version string in the skill/start guide/setup/templates, the README, and changelog together. The validator detects stale current-version strings in core release documents.
4. Rebuild and run all checks. Inspect the generated Chat edition and both ZIP layouts. Keep public API/provider guidance explicitly dated.
5. Run or repeat the relevant model-evaluation cases after any change to routing, evidence handling, or approval logic. Record actual outputs privately; publish only sanitised summaries with scope and limits.
6. Create a tagged release only after the owner reviews the content, distribution terms, and compatibility claims. Do not label an untested adapter verified.

The builder uses only standard-library Python and fixed ZIP metadata so the same canonical input produces the same archives. Build and validation scripts are release-maintenance tools, not mandatory runtime dependencies for the research skill.

## What to record for a model run

Release version and artifact hash; provider/product/surface; model as reported; relevant plan and settings; date; task ID; input fixture version; actual output location; reviewer; per-criterion outcome; critical failures; corrective change; retest reference.

Never treat a source-document review, a successful file upload, a model's claim that it loaded the skill, or passing deterministic Python tests as an independent behavioural evaluation.
