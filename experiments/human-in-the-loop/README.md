# Experiment: Human-in-the-Loop Thresholds

## Question

When should an AI system automate a decision, and when should it route the case to a human?

## Hypothesis

Confidence alone is not enough. Automation should consider confidence, risk, financial impact, and whether the action is reversible.

## Decision policy

The prototype evaluates four signals:

- Model confidence
- Risk level
- Monetary impact
- Reversibility

High-risk or irreversible actions require human review even when model confidence is high.

## Product implication

The automation boundary is a product policy, not only a model capability.

A useful operating model is:

**Low risk → automate | Medium risk → constrained automation | High risk / irreversible → human review**

See `src/human_review.py`.
