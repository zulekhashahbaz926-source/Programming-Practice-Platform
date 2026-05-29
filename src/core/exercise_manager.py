"""Exercise manager handling loading, validation, and feedback for programming exercises.

The manager interacts with :class:`src.db.repositories.ExerciseRepository` for persistence
and provides a simple API that the UI layer can consume.
"""

from typing import List, Tuple

from src.db.repositories import ExerciseRepository
from src.db.models import Exercise
from src.utils.exceptions import ValidationError


class ExerciseManager:
    """Business logic for programming exercises.

    Responsibilities
    --------------
    * Retrieve exercises by ID or category.
    * Validate a user's submitted solution against the stored reference solution.
    * Produce structured feedback (correct/incorrect) with optional hints.
    """

    def __init__(self, db_path: str | None = None):
        self._repo = ExerciseRepository(db_path) if db_path else ExerciseRepository()

    # ---------------------------------------------------------------------
    # Retrieval API
    # ---------------------------------------------------------------------
    def get_exercise(self, exercise_id: int) -> Exercise:
        """Return a single :class:`Exercise` or raise :class:`ValidationError`.
        """
        exercise = self._repo.get_exercise(exercise_id)
        if not exercise:
            raise ValidationError(f"Exercise with id {exercise_id} does not exist.")
        return exercise

    def list_exercises(self, category: str | None = None) -> List[Exercise]:
        """Return all exercises, optionally filtered by *category*.
        """
        all_ex = self._repo.list_exercises()
        if category:
            return [ex for ex in all_ex if ex.category.lower() == category.lower()]
        return all_ex

    # ---------------------------------------------------------------------
    # Validation & feedback
    # ---------------------------------------------------------------------
    def evaluate_submission(self, exercise_id: int, user_code: str) -> Tuple[bool, str]:
        """Compare *user_code* with the stored solution.

        Returns a tuple ``(is_correct, feedback)`` where ``is_correct`` is a
        boolean and ``feedback`` is a human‑readable message.  The comparison is
        simple string equality after stripping trailing whitespace – a real
        system could execute the code in a sandbox, but that is out of scope for
        this module.
        """
        exercise = self.get_exercise(exercise_id)
        expected = exercise.solution.strip()
        submitted = user_code.strip()
        if submitted == expected:
            return True, "Correct! Well done."
        # Basic hint: show first line of the expected solution.
        hint = expected.split('\n')[0] if expected else ""
        feedback = f"Incorrect. Hint: {hint}" if hint else "Incorrect."
        return False, feedback

    def add_exercise(
        self,
        title: str,
        description: str,
        solution: str,
        category: str = "Beginner",
    ) -> Exercise:
        """Create a new exercise after validating its fields.
        """
        if not title:
            raise ValidationError("Exercise title cannot be empty.")
        if category not in {"Beginner", "Intermediate", "Advanced"}:
            raise ValidationError("Invalid category; must be Beginner, Intermediate, or Advanced.")
        return self._repo.add_exercise(title, description, solution, category)
