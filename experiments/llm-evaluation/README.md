# Experiment: LLM Evaluation

## Question

How can a product evaluate AI-generated answers consistently without relying only on human spot checks?

## Hypothesis

A useful evaluation layer should score multiple dimensions separately: factual correctness, relevance, and whether the answer is supported by the available evidence.

## Experiment design

Use synthetic question-answer cases with expected answers and retrieved context.

Compare generated answers using simple, explainable checks:

- Correctness
- Relevance
- Grounding
- Overall pass rate

The evaluator is deliberately deterministic so the experiment remains reproducible. A model-based judge can later replace the scoring function without changing the evaluation contract.

## Product implication

AI quality should be measured as a product metric, not inferred from a few impressive examples.

A production system should maintain a labeled evaluation set and track quality regressions as prompts, models, retrieval systems, or workflows change.

See the executable baseline in `src/evaluate_answers.py`.
