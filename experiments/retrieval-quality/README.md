# Experiment: Retrieval Quality

## Question

How should a product evaluate whether a retrieval layer is actually finding the right evidence before an LLM generates an answer?

## Hypothesis

A retrieval system should be evaluated independently from generation. Good retrieval should consistently surface the relevant document in the top-k results, especially for queries using different wording from the source text.

## Experiment design

Use a small synthetic knowledge base and compare a lexical retrieval baseline against labeled queries.

Measure:

- **Recall@K** — whether the relevant document appears in the top K
- **MRR** — how high the first relevant result appears
- Query coverage
- Failure cases

The experiment intentionally separates:

**Retrieval quality → Generation quality → Final answer quality**

## Product implication

If the right evidence is not retrieved, improving the prompt or model may not fix the underlying product problem.

For production RAG systems, retrieval quality should therefore be treated as its own measurable product and engineering surface.

See the executable baseline in `src/retrieval_quality.py`.
