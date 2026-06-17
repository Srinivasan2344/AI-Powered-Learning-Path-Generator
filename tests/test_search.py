from app.services.search_service import semantic_search

def test_search():

    resources = [
        {
            "title": "Intro to Machine Learning",
            "content": "Machine learning basics"
        },
        {
            "title": "Python Basics",
            "content": "Learn Python"
        }
    ]

    result = semantic_search(
        "beginner machine learning",
        resources
    )

    assert result is not None