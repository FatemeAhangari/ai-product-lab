# AI Product Lab

A practical lab for experimenting with AI product patterns, evaluation, automation, and agentic systems.

This is intentionally not a collection of generic chatbot demos. Each experiment answers a product or system question and records the trade-offs.

## Experiment format

**Problem → Hypothesis → Prototype → Evaluation → Product implication**

## Experiments

### 03 — LLM Evaluation

**Question:** How can a product evaluate AI-generated answers consistently instead of relying only on human spot checks?

Measures fact coverage, grounding, relevance, and overall pass rate on labeled synthetic cases.

See:
`experiments/llm-evaluation/`

### 02 — Retrieval Quality

**Question:** How should a product evaluate whether a retrieval layer is finding the right evidence before an LLM generates an answer?

Measures Recall@K and MRR on synthetic knowledge-base queries, separating retrieval quality from generation quality.

See:
`experiments/retrieval-quality/`

### 01 — Prompt vs Rules

**Question:** When should a product use an LLM for classification, and when should deterministic rules be preferred?

The experiment compares an explicit rule-based classifier with a semantic, model-shaped baseline on synthetic operational language.

Key dimensions:
- Accuracy
- Confidence
- Ambiguous-case handling
- False automation risk

See:
`experiments/prompt-vs-rules/`

## Areas

- Structured LLM output
- Tool use
- Agent workflows
- Human-in-the-loop
- RAG and retrieval quality
- AI evaluation
- Prompt/version management
- Latency and cost
- Reliability and guardrails
- AI product metrics

## Product principle

The goal is not to maximize LLM usage.

The goal is to determine **where AI creates measurable product value** while keeping predictable decisions deterministic and safe.

## Portfolio focus

AI product management · Product experimentation · AI evaluation · Systems thinking · Automation · Technical product leadership

## Data

Experiments use public, synthetic, or generated data. No confidential company data is included.

## Status

🚧 Living portfolio / experimentation lab
