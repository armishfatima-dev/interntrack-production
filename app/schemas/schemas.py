from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
  name: str
  email: EmailStr
  role: Optional[str] = "intern"


class UserCreate(UserBase):
  pass


class UserResponse(UserBase):
  id: int

  class Config:
    from_attributes = True


class SubmissionBase(BaseModel):
  intern_id: int
  week_id: int
  status: Optional[str] = "submitted"


class SubmissionCreate(SubmissionBase):
  pass


class SubmissionResponse(SubmissionBase):
  id: int
  submitted_at: datetime

  class Config:
    from_attributes = True

