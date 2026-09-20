# Experiment: Cost & Latency Trade-offs

## Question

When is a more capable AI model worth its additional latency and cost?

## Hypothesis

Model selection should optimize for the product's quality threshold rather than raw model capability. A faster, cheaper model may be preferable when it clears the required quality bar.

## Experiment design

Compare synthetic model profiles across:

- Quality
- Latency
- Cost per 1K tokens
- Requests per minute

Calculate a simple product utility score after applying a minimum quality threshold.

This is a decision framework, not a benchmark of real models.

## Product implication

AI model selection is a product trade-off:

**Quality × Cost × Latency × Volume**

The right model depends on the workflow. Interactive customer experiences may prioritize latency, while back-office analysis may tolerate more latency for higher quality.

See `src/cost_latency.py`.
