def route_condition(screening_scores: dict):

    anxiety = screening_scores.get("anxiety", 0)
    stress = screening_scores.get("stress", 0)

    if anxiety == 0 and stress == 0:
        return "neutral"

    if anxiety >= stress:
        return "anxiety"

    return "stress"