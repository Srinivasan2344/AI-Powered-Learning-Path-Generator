def detect_knowledge_gaps(assessment_scores):
    weak_topics = []

    for topic, score in assessment_scores.items():
        if score < 60:
            weak_topics.append(topic)

    return weak_topics