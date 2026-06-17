quiz_bank = {
    "Statistics": [
        "Statistics Basics Quiz",
        "Statistics Practice Quiz"
    ],
    "Probability": [
        "Probability Beginner Quiz",
        "Probability Practice Quiz"
    ],
    "Python": [
        "Python Fundamentals Quiz"
    ],
    "Linear Algebra": [
        "Linear Algebra Revision Quiz"
    ],
    "Calculus": [
        "Calculus Review Quiz"
    ],
        "Data Structures": [
            "Data Structures Quiz"
    ],
        "Algorithms": [
            "Algorithms Quiz"
    ]
}


def recommend_quizzes(weak_topics):
    recommendations = {}

    for topic in weak_topics:
        recommendations[topic] = quiz_bank.get(
            topic,
            ["General Practice Quiz"]
        )

    return recommendations