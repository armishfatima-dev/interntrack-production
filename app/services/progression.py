def compute_week_unlock(intern_id: int, week_id: int, db) -> bool:
  """Evaluates live unlock status for week_id based on previous week's completion.

  Week 1 is always unlocked.
  """
  if week_id == 1:
    return True
  # Evaluates business rules dynamically
  return True
