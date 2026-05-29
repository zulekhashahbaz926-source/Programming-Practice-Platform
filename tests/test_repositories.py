import pytest
from src.db.repositories import UserRepository, ExerciseRepository, ProgressRepository, ChallengeRepository
from src.db.models import User, Exercise, Progress, Challenge

# User Repository Tests
def test_user_repository_crud(db):
    repo = UserRepository(db_path=db.path)
    # Create
    user = repo.add_user(username="john", password_hash="hash")
    assert isinstance(user, User)
    # Read
    fetched = repo.get_user_by_username("john")
    assert fetched.id == user.id
    # List
    users = repo.list_users()
    assert any(u.username == "john" for u in users)

# Exercise Repository Tests
def test_exercise_repository_crud(db):
    repo = ExerciseRepository(db_path=db.path)
    ex = repo.add_exercise(title="Ex1", description="Desc", solution="print('hi')", category="Beginner")
    assert isinstance(ex, Exercise)
    fetched = repo.get_exercise(ex.id)
    assert fetched.title == "Ex1"
    all_ex = repo.list_exercises()
    assert any(e.id == ex.id for e in all_ex)

# Progress Repository Tests
def test_progress_repository_crud(db):
    # Need a user and exercise first
    u_repo = UserRepository(db_path=db.path)
    e_repo = ExerciseRepository(db_path=db.path)
    user = u_repo.add_user(username="alice", password_hash="hash")
    ex = e_repo.add_exercise(title="Ex2", description="", solution="", category="Beginner")
    repo = ProgressRepository(db_path=db.path)
    prog = repo.record_progress(user_id=user.id, exercise_id=ex.id, completed=True, score=10.0)
    assert isinstance(prog, Progress)
    user_prog = repo.get_user_progress(user.id)
    assert any(p.id == prog.id for p in user_prog)

# Challenge Repository Tests
def test_challenge_repository_crud(db):
    repo = ChallengeRepository(db_path=db.path)
    ch = repo.add_challenge(title="Ch1", description="Desc", difficulty="Easy", solution="")
    assert isinstance(ch, Challenge)
    fetched = repo.get_challenge(ch.id)
    assert fetched.title == "Ch1"
    all_ch = repo.list_challenges()
    assert any(c.id == ch.id for c in all_ch)
