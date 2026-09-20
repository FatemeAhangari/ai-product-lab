import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from human_review import should_automate

def test_low_risk_high_confidence_can_automate():
    assert should_automate({
        "confidence": 0.96,
        "risk": "low",
        "amount": 100000,
        "reversible": True,
    })

def test_low_confidence_requires_human():
    assert not should_automate({
        "confidence": 0.70,
        "risk": "low",
        "amount": 100000,
        "reversible": True,
    })

def test_high_risk_requires_human_even_with_high_confidence():
    assert not should_automate({
        "confidence": 0.99,
        "risk": "high",
        "amount": 100000,
        "reversible": True,
    })

def test_high_value_irreversible_case_requires_human():
    assert not should_automate({
        "confidence": 0.99,
        "risk": "medium",
        "amount": 70000000,
        "reversible": False,
    })
