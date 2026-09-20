# Experiment: Prompt & Model Regression

## Question

How can a product detect quality regressions when a prompt or model version changes?

## Hypothesis

Every production change should be evaluated against a fixed regression set before release. A change that improves one example but degrades overall quality should not silently ship.

## Experiment design

Compare two synthetic versions against the same labeled evaluation set.

Measure:

- Overall pass rate
- Per-case results
- Regressions
- Improvements
- Release decision

The evaluator is deterministic for reproducibility.

## Product implication

AI systems need version-aware product operations:

**Change → Evaluate → Compare → Approve / Reject**

Prompt and model changes should be treated as product releases with measurable acceptance criteria.

See `src/regression.py`.
