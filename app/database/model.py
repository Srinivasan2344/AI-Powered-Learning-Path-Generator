from sqlalchemy import Column, Integer, String, ForeignKey,Base


class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer)
    topic = Column(String)
    score = Column(Integer)