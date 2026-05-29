"""Progress tracker handling user performance data for exercises.

The tracker interacts with :class:`src.db.repositories.ProgressRepository` for persistence
and provides a simple API that the UI layer can consume.
"""

from typing import List, Tuple

from src.db.repositories import ProgressRepository, UserRepository
from src.db.models import Progress
from src.utils.exceptions import ValidationError


class ProgressTracker:
    """Business logic for tracking and analyzing user progress.

    Responsibilities
    --------------
    * Record progress for a user on a given exercise.
    * Retrieve all progress entries for a user.
    * Compute simple statistics such as completion rate and average score.
    """

    def __init__(self, db_path: str | None = None):
        self._progress_repo = ProgressRepository(db_path) if db_path else ProgressRepository()
        self._user_repo = UserRepository(db_path) if db_path else UserRepository()

    # ---------------------------------------------------------------------
    # Recording API
    # ---------------------------------------------------------------------
    def record_progress(
        self,
        username: str,
        exercise_id: int,
        completed: bool,
        score: float = 0.0,
    ) -> Progress:
        """Validate user existence and store a progress record.

        Raises
        ------
        ValidationError
            If the username does not correspond to an existing user.
        """
        user = self._user_repo.get_user_by_username(username)
        if not user:
            raise ValidationError(f"User '{username}' does not exist.")
        return self._progress_repo.record_progress(
            user_id=user.id,
            exercise_id=exercise_id,
            completed=completed,
            score=score,
        )

    def get_user_progress(self, username: str) -> List[Progress]:
        """Return all :class:`Progress` entries for *username*.

        Raises
        ------
        ValidationError
            If the user does not exist.
        """
        user = self._user_repo.get_user_by_username(username)
        if not user:
            raise ValidationError(f"User '{username}' does not exist.")
        return self._progress_repo.get_user_progress(user.id)

    # ---------------------------------------------------------------------
    # Statistics API
    # ---------------------------------------------------------------------
    def compute_statistics(self, username: str) -> Tuple[float, float]:
        """Calculate and return ``(completion_rate, average_score)``.

        * **completion_rate** – proportion of completed exercises (0‑1).
        * **average_score** – mean score across all recorded attempts.
        """
        progress_entries = self.get_user_progress(username)
        if not progress_entries:
            return 0.0, 0.0
        total = len(progress_entries)
        completed = sum(1 for p in progress_entries if p.completed)
        avg_score = sum(p.score for p in progress_entries) / total
        return completed / total, avg_score
