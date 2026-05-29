"""Challenge manager handling dynamic coding challenges.

The manager works with :class:`src.db.repositories.ChallengeRepository` to fetch
pre‑defined challenges and with :class:`src.db.repositories.ExerciseRepository`
to provide an associated exercise. It records attempt results via
:class:`src.db.repositories.ProgressRepository` and tracks per‑session usage
to avoid repetition.
"""

import random
from typing import Dict, List, Tuple

from src.db.repositories import (
    ChallengeRepository,
    ExerciseRepository,
    ProgressRepository,
    UserRepository,
)
from src.db.models import Challenge, Exercise, Progress
from src.utils.exceptions import ValidationError


class ChallengeManager:
    """Business logic for generating and handling coding challenges.

    Features
    --------
    * Generate a random challenge based on *difficulty* (Easy, Medium, Hard).
    * Pair each challenge with an exercise drawn from the corresponding
      category (Beginner ↔ Easy, Intermediate ↔ Medium, Advanced ↔ Hard).
    * Ensure a challenge is not repeated within the same manager session.
    * Assign score weights according to difficulty.
    * Track the number of attempts per challenge for the current session.
    * Persist attempt results via :class:`ProgressRepository`.
    * Raise :class:`ValidationError` for invalid inputs.
    """

    # Score multipliers for each difficulty level – can be tuned later.
    _SCORE_WEIGHTS: Dict[str, float] = {
        "Easy": 1.0,
        "Medium": 1.5,
        "Hard": 2.0,
    }

    # Mapping from challenge difficulty to exercise category.
    _CATEGORY_MAP: Dict[str, str] = {
        "Easy": "Beginner",
        "Medium": "Intermediate",
        "Hard": "Advanced",
    }

    def __init__(self, db_path: str | None = None) -> None:
        """Create a manager instance.

        Parameters
        ----------
        db_path: Optional path to the SQLite database. If omitted the default
                 path defined in the repositories is used.
        """
        self._challenge_repo = ChallengeRepository(db_path) if db_path else ChallengeRepository()
        self._exercise_repo = ExerciseRepository(db_path) if db_path else ExerciseRepository()
        self._progress_repo = ProgressRepository(db_path) if db_path else ProgressRepository()
        self._user_repo = UserRepository(db_path) if db_path else UserRepository()
        # Keep track of challenge IDs that have already been served in this session.
        self._used_challenge_ids: set[int] = set()
        # Count attempts per challenge for the active session.
        self._attempt_counts: Dict[int, int] = {}

    # ---------------------------------------------------------------------
    # Private helpers
    # ---------------------------------------------------------------------
    def _validate_difficulty(self, difficulty: str) -> str:
        """Normalize and validate *difficulty*.

        Returns the title‑cased difficulty if valid, otherwise raises
        :class:`ValidationError`.
        """
        normalized = difficulty.strip().title()
        if normalized not in self._SCORE_WEIGHTS:
            raise ValidationError(
                f"Invalid difficulty '{difficulty}'. Expected one of: "
                f"{', '.join(self._SCORE_WEIGHTS.keys())}."
            )
        return normalized

    def _pick_unused_challenge(self, challenges: List[Challenge]) -> Challenge:
        """Return a random challenge that has not been used in this session.

        If all challenges have already been used, the used‑set is cleared so the
        pool can be reused.
        """
        available = [c for c in challenges if c.id not in self._used_challenge_ids]
        if not available:
            # All challenges exhausted – start a new cycle.
            self._used_challenge_ids.clear()
            available = challenges
        challenge = random.choice(available)
        self._used_challenge_ids.add(challenge.id)
        return challenge

    def _get_exercise_for_difficulty(self, difficulty: str) -> Exercise:
        """Select a random exercise that matches the difficulty's category.
        """
        category = self._CATEGORY_MAP[difficulty]
        exercises = self._exercise_repo.list_exercises(category)
        if not exercises:
            raise ValidationError(
                f"No exercises found for category '{category}'."
            )
        return random.choice(exercises)

    # ---------------------------------------------------------------------
    # Public API
    # ---------------------------------------------------------------------
    def get_challenge(self, difficulty: str) -> Tuple[Challenge, Exercise]:
        """Generate a challenge and a matching exercise.

        Parameters
        ----------
        difficulty: ``"Easy"``, ``"Medium"`` or ``"Hard"``.

        Returns
        -------
        tuple[Challenge, Exercise]
            The selected challenge together with a related exercise.
        """
        norm_diff = self._validate_difficulty(difficulty)
        # Fetch all challenges of the requested difficulty.
        all_challenges = [c for c in self._challenge_repo.list_challenges() if c.difficulty == norm_diff]
        if not all_challenges:
            raise ValidationError(f"No challenges available for difficulty '{norm_diff}'.")
        challenge = self._pick_unused_challenge(all_challenges)
        exercise = self._get_exercise_for_difficulty(norm_diff)
        # Initialise attempt count for this challenge.
        self._attempt_counts[challenge.id] = 0
        return challenge, exercise

    def submit_challenge(
        self,
        username: str,
        challenge_id: int,
        completed: bool,
        score: float = 0.0,
    ) -> Progress:
        """Record a user's attempt for a specific challenge.

        The *score* supplied by the caller is multiplied by the difficulty‑
        specific weight before persisting.
        """
        user = self._user_repo.get_user_by_username(username)
        if not user:
            raise ValidationError(f"User '{username}' does not exist.")
        # Retrieve the challenge to obtain its difficulty for weighting.
        challenge = self._challenge_repo.get_challenge(challenge_id)
        if not challenge:
            raise ValidationError(f"Challenge with id {challenge_id} not found.")
        # Update attempt counter.
        self._attempt_counts[challenge_id] = self._attempt_counts.get(challenge_id, 0) + 1
        # Apply weight.
        weight = self._SCORE_WEIGHTS[challenge.difficulty]
        weighted_score = score * weight
        # Persist the attempt. We reuse the ProgressRepository – the *exercise_id*
        # field stores the challenge id for traceability (foreign‑key constraints
        # are not enforced for this cross‑entity relationship).
        progress = self._progress_repo.record_progress(
            user_id=user.id,
            exercise_id=challenge.id,
            completed=completed,
            score=weighted_score,
        )
        return progress

    def get_attempt_count(self, challenge_id: int) -> int:
        """Return the number of attempts made for *challenge_id* in the current session.
        """
        return self._attempt_counts.get(challenge_id, 0)

    def compute_challenge_score(self, difficulty: str, raw_score: float) -> float:
        """Utility to calculate the weighted score for a given difficulty.
        """
        norm_diff = self._validate_difficulty(difficulty)
        return raw_score * self._SCORE_WEIGHTS[norm_diff]

    # ---------------------------------------------------------------------
    # Extensibility hooks (future features)
    # ---------------------------------------------------------------------
    def get_leaderboard(self, difficulty: str | None = None):
        """Placeholder for future leaderboard functionality.
        """
        raise NotImplementedError("Leaderboard feature is not yet implemented.")

    def get_daily_challenge(self):
        """Placeholder for future daily‑challenge generation.
        """
        raise NotImplementedError("Daily challenge feature is not yet implemented.")

    def get_multiplayer_match(self, usernames: List[str]):
        """Placeholder for future multiplayer battle matchmaking.
        """
        raise NotImplementedError("Multiplayer battles are not yet implemented.")
