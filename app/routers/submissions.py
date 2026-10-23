from typing import List, Optional
from app.database import get_db
from app.models.models import Submission, User
from app.schemas.schemas import SubmissionCreate, SubmissionResponse
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session, joinedload

router = APIRouter(prefix="/submissions", tags=["Submissions"])


@router.get(
    "/",
    response_model=List[SubmissionResponse],
    summary="List Submissions",
    description=(
        "Retrieve submissions with eager loading optimization (fixing N+1 query"
        " problem) and pagination."
    ),
)
def get_submissions(
    status: Optional[str] = Query(None, description="Filter submissions by status"),
    skip: int = Query(0, description="Records to skip"),
    limit: int = Query(10, description="Records to return"),
    db: Session = Depends(get_db),
):
  # Optimized with joinedload to prevent N+1 queries
  query = db.query(Submission).options(joinedload(Submission.intern))
  if status:
    query = query.filter(Submission.status == status)
  return query.offset(skip).limit(limit).all()


@router.post(
    "/",
    response_model=SubmissionResponse,
    summary="Create Submission",
    description="Create a new task submission for an intern.",
)
def create_submission(payload: SubmissionCreate, db: Session = Depends(get_db)):
  new_sub = Submission(**payload.dict())
  db.add(new_sub)
  db.commit()
  db.refresh(new_sub)
  return new_sub

