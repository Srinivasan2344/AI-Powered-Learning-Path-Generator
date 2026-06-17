import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)
import textstat


def evaluate_content(content: str):

    readability = textstat.flesch_reading_ease(content)

    suggestions = []

    if readability < 50:
        suggestions.append(
            "Simplify sentence structure for better readability."
        )

    if len(content.split()) < 10:
        suggestions.append(
            "Provide more detailed explanations."
        )

    return {
        "readability_score": round(readability, 2),
        "suggestions": suggestions,
        "content_length": len(content.split())
    }