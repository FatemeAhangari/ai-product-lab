from pathlib import Path
import json
import math
import re
from collections import Counter

ROOT = Path(__file__).parents[2]

def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())

def load_json(path: Path):
    return json.loads(path.read_text())

def score(query: str, document: dict) -> float:
    q = Counter(tokenize(query))
    d = Counter(tokenize(document["title"] + " " + document["text"]))
    return sum(min(q[token], d[token]) for token in q)

def retrieve(query: str, documents: list[dict], k: int = 3) -> list[dict]:
    ranked = sorted(documents, key=lambda doc: score(query, doc), reverse=True)
    return ranked[:k]

def recall_at_k(results: list[list[dict]], relevant_ids: list[str]) -> float:
    hits = sum(
        any(doc["id"] == relevant_id for doc in docs)
        for docs, relevant_id in zip(results, relevant_ids)
    )
    return hits / len(relevant_ids) if relevant_ids else 0.0

def reciprocal_rank(docs: list[dict], relevant_id: str) -> float:
    for rank, doc in enumerate(docs, start=1):
        if doc["id"] == relevant_id:
            return 1 / rank
    return 0.0

def mean_reciprocal_rank(results: list[list[dict]], relevant_ids: list[str]) -> float:
    scores = [
        reciprocal_rank(docs, relevant_id)
        for docs, relevant_id in zip(results, relevant_ids)
    ]
    return sum(scores) / len(scores) if scores else 0.0

def run(k: int = 3) -> dict[str, float]:
    docs = load_json(ROOT / "data/knowledge_base.json")
    queries = load_json(ROOT / "data/evaluation_queries.json")
    results = [retrieve(item["query"], docs, k=k) for item in queries]
    relevant_ids = [item["relevant_id"] for item in queries]

    return {
        "recall_at_k": recall_at_k(results, relevant_ids),
        "mrr": mean_reciprocal_rank(results, relevant_ids),
    }

if __name__ == "__main__":
    print(run(k=3))
