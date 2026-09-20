import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from cost_latency import utility

def test_model_below_quality_threshold_is_rejected():
    profile = {
        "quality": 0.80,
        "latency_ms": 300,
        "cost_per_1k_tokens": 0.001,
        "requests_per_minute": 100,
    }
    assert utility(profile, min_quality=0.85) == 0.0

def test_balanced_profile_gets_nonzero_utility():
    profile = {
        "quality": 0.88,
        "latency_ms": 850,
        "cost_per_1k_tokens": 0.006,
        "requests_per_minute": 80,
    }
    assert utility(profile, min_quality=0.85) > 0.0

def test_higher_latency_reduces_utility():
    fast = {
        "quality": 0.88,
        "latency_ms": 400,
        "cost_per_1k_tokens": 0.006,
        "requests_per_minute": 80,
    }
    slow = {
        "quality": 0.88,
        "latency_ms": 1600,
        "cost_per_1k_tokens": 0.006,
        "requests_per_minute": 80,
    }
    assert utility(fast) > utility(slow)
