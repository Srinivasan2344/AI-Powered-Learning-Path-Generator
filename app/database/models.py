from sqlalchemy import Column, Integer, String
from app.database.connection import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, unique=True, index=True)
    goal = Column(String)
    available_hours_per_week = Column(Integer)


class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, index=True)
    topic = Column(String)
    score = Column(Integer)