course_graph = {
    "Machine Learning": ["Statistics", "Linear Algebra", "Python"],
    "Deep Learning": ["Machine Learning"],
    "NLP": ["Machine Learning", "Python"]
}


def generate_learning_path(student):
    goal = student.goal

    prerequisites = course_graph.get(goal, [])

    learning_path = []

    for topic in prerequisites:
        score = student.assessment_scores.get(topic, 0)

        if score < 60:
            learning_path.append(f"Revise {topic}")
        else:
            learning_path.append(topic)

    learning_path.append(goal)

    return learning_path


def generate_learning_path(student):
    goal = student.goal

    prerequisites = course_graph.get(goal, [])

    learning_path = []

    for topic in prerequisites:
        score = student.assessment_scores.get(topic, 0)

        if score < 60:
            learning_path.append(f"Revise {topic}")
        else:
            learning_path.append(topic)

    learning_path.append(goal)

    return learning_path


def generate_study_schedule(learning_path, hours_per_week):
    schedule = []

    for week, topic in enumerate(learning_path, start=1):
        schedule.append({
            "week": week,
            "topic": topic,
            "recommended_hours": hours_per_week
        })

    return schedule