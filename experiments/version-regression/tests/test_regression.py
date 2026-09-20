import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from regression import compare

def test_regression_is_detected():
    cases = [
        {"id":"1","expected":"booking","v1":"booking","v2":"refund"}
    ]
    result = compare(cases)
    assert result["regressions"] == ["1"]
    assert result["release"] == "review"

def test_improvement_is_detected():
    cases = [
        {"id":"1","expected":"booking","v1":"unknown","v2":"booking"}
    ]
    result = compare(cases)
    assert result["improvements"] == ["1"]
    assert result["release"] == "approve"
