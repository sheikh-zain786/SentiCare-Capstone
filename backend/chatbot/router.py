
_QUESTION_COUNTS = {
    "anxiety":    3,   # feeling_nervous, uncontrollable_worry, restlessness
    "depression": 3,   # feeling_down, loss_of_interest, fatigue
    "stress":     2,   # overwhelmed, irritability
}

# Minimum AVERAGE score (0-3 scale) needed to route to a condition.
# 0.8 = roughly "several days on at least one question" — meaningful signal.
_MIN_AVG = 0.8

# Tie-break priority
_PRIORITY = ["anxiety", "stress", "depression"]


def route_condition(screening_scores: dict) -> str:
    averages = {}
    for condition in ("anxiety", "stress", "depression"):
        raw = screening_scores.get(condition, 0)
        count = _QUESTION_COUNTS.get(condition, 1)
        avg = raw / count
        if avg >= _MIN_AVG:
            averages[condition] = avg

    print(
        f"[router] raw={screening_scores}  "
        f"averages={averages}  "
        f"min_avg={_MIN_AVG}",
        flush=True,
    )

    if not averages:
        return "neutral"

    top_avg = max(averages.values())

    # Allow a small tolerance for "tie" — within 0.1 of each other
    tied = [k for k, v in averages.items() if abs(v - top_avg) < 0.1]

    if len(tied) == 1:
        return tied[0]

    for condition in _PRIORITY:
        if condition in tied:
            return condition

    return tied[0]