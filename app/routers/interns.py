from typing import List, Optional
from app.database import get_db
from app.models.models import User
from app.schemas.schemas import UserResponse
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

router = APIRouter(prefix="/interns", tags=["Interns"])


@router.get(
    "/",
    response_model=List[UserResponse],
    summary="List Interns",
    description=(
        "Retrieve a paginated list of all registered interns with optional"
        " case-insensitive search."
    ),
)
def get_interns(
    search: Optional[str] = Query(
        None, description="Search term for name or email"
    ),
    skip: int = Query(0, description="Number of records to skip for pagination"),
    limit: int = Query(10, description="Maximum number of records to return"),
    db: Session = Depends(get_db),
):
  query = db.query(User)
  if search:
    query = query.filter(
        User.name.ilike(f"%{search}%") | User.email.ilike(f"%{search}%")
    )
  return query.offset(skip).limit(limit).all()

