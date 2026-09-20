import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from prompt_vs_rules import rule_classifier, semantic_baseline


def test_rules_handle_explicit_language():
    result = rule_classifier("Customer requests a refund")
    assert result.prediction == "refund"


def test_semantic_baseline_handles_paraphrase():
    result = semantic_baseline("Customer wants reimbursement after a cancelled trip")
    assert result.prediction == "refund"


def test_unknown_stays_low_confidence():
    result = semantic_baseline("Customer has an unrelated question")
    assert result.prediction == "unknown"
    assert result.confidence < 0.5
