def determine_risk_level(score):
    if score <= 6:
        return "LOW"
    elif score <= 12:
        return "MODERATE"
    else:
        return "HIGH"
