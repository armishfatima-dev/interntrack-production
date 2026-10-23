from app.database import Base
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text, Index
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  email = Column(String, unique=True, index=True)
  role = Column(String, default="intern")


class Submission(Base):
  __tablename__ = "submissions"

  id = Column(Integer, primary_key=True, index=True)
  intern_id = Column(Integer, ForeignKey("users.id"), index=True)
  week_id = Column(Integer, index=True)
  status = Column(String, default="submitted", index=True) # submitted, graded, etc.
  submitted_at = Column(DateTime, default=datetime.utcnow)

  intern = relationship("User", backref="submissions")


# Explicit indexes for performance optimization
Index("idx_submission_intern_week", Submission.intern_id, Submission.week_id)

