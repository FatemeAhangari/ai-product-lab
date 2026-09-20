from dataclasses import dataclass


@dataclass
class Result:
    method: str
    prediction: str
    confidence: float


def rule_classifier(text: str) -> Result:
    text = text.lower()

    if "refund" in text or "money back" in text:
        return Result("rules", "refund", 0.95)
    if "booking" in text or "reservation" in text:
        return Result("rules", "booking", 0.90)
    if "provider" in text or "supplier" in text:
        return Result("rules", "provider", 0.90)

    return Result("rules", "unknown", 0.40)


def semantic_baseline(text: str) -> Result:
    """Model-shaped baseline with a replaceable interface.

    This is intentionally offline and deterministic. A real LLM can replace
    this function while preserving the experiment contract.
    """
    text = text.lower()

    if any(word in text for word in ["reimburse", "reimbursement", "cancelled trip"]):
        return Result("semantic_baseline", "refund", 0.86)
    if any(word in text for word in ["confirmation", "reservation", "payment"]):
        return Result("semantic_baseline", "booking", 0.84)
    if any(word in text for word in ["supplier", "timeout", "vendor"]):
        return Result("semantic_baseline", "provider", 0.82)

    return Result("semantic_baseline", "unknown", 0.35)
