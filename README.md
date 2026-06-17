# AI-Powered Learning Platform

# Project Overview

AI-Powered Learning Platform is a FastAPI-based application that provides personalized learning recommendations, knowledge gap analysis, quiz recommendations, engagement prediction, semantic search, content quality evaluation, and AI performance monitoring.

The platform helps students improve their learning experience through intelligent recommendations and analytics.

---

# Features

# Personalized Learning Path Generator
- Generates learning paths based on student goals
- Recommends relevant topics
- Tracks learning progress

# Knowledge Gap Analysis
- Identifies weak subject areas
- Analyzes assessment performance
- Suggests improvement areas

# Intelligent Quiz Recommendation
- Recommends quizzes based on learning needs
- Supports personalized practice

# Student Engagement Prediction
- Analyzes login frequency
- Tracks assignment completion
- Predicts engagement risk levels

# Smart Content Classification
- Classifies educational content
- Detects subject and difficulty level
- Extracts important keywords

# Content Quality Evaluation
- Calculates readability scores
- Provides content improvement suggestions

# Semantic Search Engine
- Supports natural language queries
- Retrieves relevant educational resources

# AI Performance Monitoring
- Monitors CPU usage
- Monitors memory usage
- Generates system performance metrics

---

# Technology Stack

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic
- Pytest
- Textstat
- Psutil
- Pandas
- Scikit-Learn

---

# Project Structure

```text
app/
├── api/
├── database/
├── models/
├── schemas/
├── services/
├── utils/
└── main.py

tests/
├── test_content_quality.py
├── test_engagement.py
├── test_learning_path.py
└── test_search.py
```

---

# Installation

# Clone Repository

```bash
git clone https://github.com/Srinivasan2344/AI-Powered-Learning-Platform.git
cd AI-Powered-Learning-Platform
```

# Create Virtual Environment

```bash
python -m venv .venv
```

# Activate Environment

```bash
.venv\Scripts\activate
```

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
uvicorn app.main:app --reload
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs

# Running Tests

```bash
pytest -v
```

Test Results:

```text
4 Tests Passed

# API Modules

- Learning Path API
- Knowledge Gap API
- Quiz Recommendation API
- Engagement Prediction API
- Content Quality API
- Semantic Search API
- Performance Monitoring API

This project is developed for educational and learning purposes.
