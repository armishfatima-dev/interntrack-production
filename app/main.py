from app.database import Base, engine, get_db
from app.routers import interns, submissions
from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

# Automatically create tables on startup for smooth development and testing
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="InternTrack API",
    description=(
        "A comprehensive backend service for managing internships,"
        " submissions, grading, progression rules, and automated notifications."
    ),
    version="1.0.0",
    terms_of_service="https://example.com/terms/",
    contact={
        "name": "InternTrack Support",
        "email": "support@interntrack.internal",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_tags=[
        {
            "name": "Interns",
            "description": (
                "Operations pertaining to intern accounts and progress"
                " tracking."
            ),
        },
        {
            "name": "Submissions",
            "description": (
                "Manage weekly task submissions, filtering, and pagination."
            ),
        },
        {
            "name": "System",
            "description": "Health checks and system diagnostics.",
        },
    ],
)

app.include_router(interns.router)
app.include_router(submissions.router)


@app.get(
    "/health",
    tags=["System"],
    summary="Health Check",
    description="Reports application health and database connectivity status.",
)
def health_check(db: Session = Depends(get_db)):
  try:
    db.execute(text("SELECT 1"))
    db_status = "connected"
  except Exception as e:
    db_status = f"disconnected: {str(e)}"

  return {
      "status": "healthy" if db_status == "connected" else "unhealthy",
      "database": db_status,
      "environment": "production",
  }

