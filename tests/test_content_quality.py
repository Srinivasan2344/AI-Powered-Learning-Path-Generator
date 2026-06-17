from app.services.content_quality_service import evaluate_content


def test_evaluate_content():
    result = evaluate_content(
        "Machine learning is a branch of AI."
    )

    assert "readability_score" in result
    assert "suggestions" in result