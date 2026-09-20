from pathlib import Path
import json

ROOT = Path(__file__).parents[2]

def evaluate_version(cases: list[dict], version: str) -> dict:
    correct = [
        case for case in cases
        if case[version] == case["expected"]
    ]
    return {
        "version": version,
        "passed": len(correct),
        "total": len(cases),
        "pass_rate": len(correct) / len(cases) if cases else 0.0,
    }

def compare(cases: list[dict], baseline: str = "v1", candidate: str = "v2") -> dict:
    regressions = [
        case["id"]
        for case in cases
        if case[baseline] == case["expected"]
        and case[candidate] != case["expected"]
    ]
    improvements = [
        case["id"]
        for case in cases
        if case[baseline] != case["expected"]
        and case[candidate] == case["expected"]
    ]

    baseline_result = evaluate_version(cases, baseline)
    candidate_result = evaluate_version(cases, candidate)

    return {
        "baseline": baseline_result,
        "candidate": candidate_result,
        "regressions": regressions,
        "improvements": improvements,
        "release": "approve" if not regressions else "review",
    }

if __name__ == "__main__":
    cases = json.loads((ROOT / "data/regression_cases.json").read_text())
    print(compare(cases))
