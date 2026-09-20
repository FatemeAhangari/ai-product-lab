RISK_ORDER = {"low": 1, "medium": 2, "high": 3}
HIGH_VALUE_THRESHOLD = 50_000_000
CONFIDENCE_THRESHOLD = 0.90

def should_automate(case: dict) -> bool:
    if case["confidence"] < CONFIDENCE_THRESHOLD:
        return False

    if RISK_ORDER[case["risk"]] >= RISK_ORDER["high"]:
        return False

    if case["amount"] >= HIGH_VALUE_THRESHOLD and not case["reversible"]:
        return False

    return True

def decide(case: dict) -> dict:
    automated = should_automate(case)
    return {
        "id": case["id"],
        "decision": "automate" if automated else "human_review",
        "reason": (
            "Case meets automation policy."
            if automated
            else "Case exceeds the defined automation boundary."
        ),
    }

if __name__ == "__main__":
    import json
    from pathlib import Path

    root = Path(__file__).parents[2]
    cases = json.loads((root / "data/cases.json").read_text())
    for case in cases:
        print(decide(case))
