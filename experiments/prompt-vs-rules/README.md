# Experiment: Prompt vs Rules

## Question

When should a product use an LLM for classification, and when should deterministic rules be preferred?

## Hypothesis

Deterministic rules are preferable for stable, explicit, high-risk decisions. LLMs are more useful when inputs are ambiguous, unstructured, or linguistically variable.

## Experiment design

Compare two approaches on the same synthetic support cases:

- **Rules:** keyword/pattern matching
- **LLM-style interpretation:** semantic intent interface with confidence

Measure:

- Accuracy
- Confidence
- Ambiguous-case handling
- False automation risk

## Product implication

The goal is not to maximize LLM usage. The product should place intelligence where it creates value while keeping predictable decisions deterministic.

See the executable baseline in `src/prompt_vs_rules.py`.
