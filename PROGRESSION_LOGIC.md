# Week Progression Logic & Evaluation Rules

## Core Business Logic

1. **Week 1 Access:** Unlocked by default for all registered interns upon creation.
2. **Subsequent Weeks (Week $N$):** Week $N$ is dynamically unlocked if and only if:
   - Week $N-1$ task submission has been completed and marked as `graded` or `submitted`.
   - The intern achieves a passing score ($\ge 70\%$) on Week $N-1$'s assessment.

## State Calculation

- Status is computed dynamically on read requests rather than storing static boolean flags in PostgreSQL, ensuring data integrity if submissions are modified or reassessed.
