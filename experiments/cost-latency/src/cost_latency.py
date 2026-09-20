from pathlib import Path
import json

ROOT = Path(__file__).parents[2]

def utility(profile: dict, min_quality: float = 0.85) -> float:
    if profile["quality"] < min_quality:
        return 0.0

    quality_value = profile["quality"]
    latency_penalty = min(profile["latency_ms"] / 2000, 1.0)
    cost_penalty = min(profile["cost_per_1k_tokens"] / 0.025, 1.0)

    return round(
        0.60 * quality_value
        + 0.20 * (1 - latency_penalty)
        + 0.20 * (1 - cost_penalty),
        3,
    )

def rank_profiles(min_quality: float = 0.85) -> list[dict]:
    profiles = json.loads((ROOT / "data/model_profiles.json").read_text())

    for profile in profiles:
        profile["utility"] = utility(profile, min_quality)

    return sorted(profiles, key=lambda item: item["utility"], reverse=True)

if __name__ == "__main__":
    for profile in rank_profiles():
        print(profile)
