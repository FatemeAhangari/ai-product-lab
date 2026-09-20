import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from evaluate_answers import fact_coverage, grounding_score

def test_fact_coverage():
    assert fact_coverage("fare rules and cancellation timing apply", ["fare rules", "cancellation timing"]) == 1.0

def test_grounding_is_zero_for_unrelated_answer():
    assert grounding_score("weather tomorrow", "refund policy") == 0.0

def test_missing_fact_reduces_coverage():
    assert fact_coverage("fare rules apply", ["fare rules", "cancellation timing"]) == 0.5
