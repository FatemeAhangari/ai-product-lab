import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from retrieval_quality import retrieve, recall_at_k

def test_retrieval_returns_requested_k():
    docs = [
        {"id":"1","title":"Refund","text":"refund policy"},
        {"id":"2","title":"Booking","text":"booking confirmation"},
        {"id":"3","title":"Provider","text":"provider timeout"},
    ]
    assert len(retrieve("refund", docs, k=2)) == 2

def test_recall_is_perfect_for_exact_signal():
    docs = [
        {"id":"1","title":"Refund","text":"refund policy"},
        {"id":"2","title":"Booking","text":"booking confirmation"},
    ]
    results = [retrieve("refund", docs, k=1)]
    assert recall_at_k(results, ["1"]) == 1.0
