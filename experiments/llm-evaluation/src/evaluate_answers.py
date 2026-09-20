from pathlib import Path
import json
import re

ROOT = Path(__file__).parents[2]

def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", text.lower())

def fact_coverage(answer: str, expected_facts: list[str]) -> float:
    normalized = normalize(answer)
    if not expected_facts:
        return 1.0
    hits = sum(fact.lower() in normalized for fact in expected_facts)
    return hits / len(expected_facts)

def grounding_score(answer: str, context: str) -> float:
    answer_tokens = set(normalize(answer).split())
    context_tokens = set(normalize(context).split())
    if not answer_tokens:
        return 0.0
    return len(answer_tokens & context_tokens) / len(answer_tokens)

def evaluate(case: dict) -> dict:
    coverage = fact_coverage(case["answer"], case["expected_facts"])
    grounding = grounding_score(case["answer"], case["context"])
    relevance = 1.0 if case["question"].split()[0].lower() in normalize(case["answer"]) else 0.0

    overall = (0.5 * coverage + 0.3 * grounding + 0.2 * relevance)

    return {
        "id": case["id"],
        "fact_coverage": round(coverage, 3),
        "grounding": round(grounding, 3),
        "relevance": round(relevance, 3),
        "overall": round(overall, 3),
        "passed": overall >= 0.70,
    }

def run() -> list[dict]:
    cases = json.loads((ROOT / "data/evaluation_cases.json").read_text())
    return [evaluate(case) for case in cases]

if __name__ == "__main__":
    results = run()
    for result in results:
        print(result)
