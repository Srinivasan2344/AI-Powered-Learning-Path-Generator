def generate_engagement_strategy(risk_level):
    strategies = {
        "High": [
            "Send personalized reminders",
            "Schedule instructor intervention",
            "Recommend shorter learning sessions"
        ],
        "Medium": [
            "Recommend weekly goals",
            "Increase quiz participation"
        ],
        "Low": [
            "Encourage advanced topics",
            "Maintain current learning pace"
        ]
    }

    return strategies.get(risk_level, [])