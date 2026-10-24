"""Simple result prediction logic for the GitHub Actions CI demo."""


def predict_result(internal_marks: int, attendance: int) -> str:
    """Return PASS when marks are at least 40 and attendance at least 75."""
    if internal_marks >= 40 and attendance >= 75:
        return "PASS"
    return "FAIL"
