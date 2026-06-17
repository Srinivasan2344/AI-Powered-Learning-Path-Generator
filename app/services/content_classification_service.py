import re


def classify_content(content: str):

    text = content.lower()

    if any(word in text for word in ["python", "java", "function", "loop"]):
        subject = "Programming"
    elif any(word in text for word in ["machine learning", "neural", "ai"]):
        subject = "Artificial Intelligence"
    elif any(word in text for word in ["algebra", "equation", "calculus"]):
        subject = "Mathematics"
    else:
        subject = "General"

    word_count = len(content.split())

    if word_count < 20:
        difficulty = "Beginner"
    elif word_count < 50:
        difficulty = "Intermediate"
    else:
        difficulty = "Advanced"

    keywords = re.findall(r"\b[a-zA-Z]{4,}\b", content)

    return {
        "subject": subject,
        "difficulty": difficulty,
        "keywords": list(set(keywords[:5]))
    }