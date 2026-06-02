import bcrypt
from datetime import datetime
from core.logger import app_logger

MODULES = [
    {
        "title": "Waterfall Model",
        "description": "Sequential software process with defined phases.",
        "category": "Process Models",
        "content": "Waterfall enforces planning, design, implementation, testing, and maintenance in linear order."
    },
    {
        "title": "Agile Model",
        "description": "Iterative and incremental development process.",
        "category": "Process Models",
        "content": "Agile supports adaptive planning, early delivery, and continuous improvement."
    },
    {
        "title": "Spiral Model",
        "description": "Risk-driven process with repeated cycles.",
        "category": "Process Models",
        "content": "Spiral blends prototyping and waterfall staging for large, high-risk systems."
    },
    {
        "title": "Version Control Practice",
        "description": "Simulated Git workflows for tracking changes.",
        "category": "Version Control",
        "content": "Commit history, branching, and message logging are simulated to teach VCS concepts."
    },
]

SAMPLE_COMMITS = [
    ("main", "Initialize Zyntriva CodeForge architecture", "system"),
    ("feature/auth", "Add secure login and signup flow", "system"),
    ("feature/dashboard", "Build futuristic dashboard overview", "system"),
    ("feature/testing", "Seed test cases and unit testing module", "system"),
    ("release/v1.0", "Provide base release with module navigation", "system"),
]

SAMPLE_NOTIFICATIONS = [
    ("New module available", "Process Model Learning has been updated with new content."),
    ("Dashboard optimized", "Performance improvements applied across the UI."),
    ("Peer Review scheduled", "A new review checklist is ready for your team."),
    ("Testing lab refreshed", "Automated testing examples are available in the Testing module."),
]

SAMPLE_REVIEWS = [
    ("Code Quality Walkthrough", "Completed", "Module Team", "Review of refactoring and code smells."),
    ("Peer Feedback Round", "In Progress", "Review Board", "Team feedback session for sprint improvements."),
]

SAMPLE_TESTS = [
    ("Authentication validation", "Passed", "OK", "Login and registration validation logic."),
    ("Database integrity", "Passed", "OK", "SQLite insert and query operations."),
    ("UI navigation", "Passed", "OK", "Dashboard and module routing behavior."),
]

def seed_sample_data(db):
    try:
        user = db.find_user_by_username("codeforge")
        if not user:
            password_hash = bcrypt.hashpw("Admin@1234".encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
            db.create_user(
                full_name="Zyntriva Administrator",
                username="codeforge",
                email="admin@zyntriva.com",
                password=password_hash,
            )
            app_logger.info("Seeded default administrator user.")

        existing = db.fetchone("SELECT id FROM quizzes LIMIT 1")
        if not existing:
            for entry in MODULES:
                db.execute(
                    "INSERT INTO quizzes (title, description, category, content) VALUES (?, ?, ?, ?)",
                    (entry["title"], entry["description"], entry["category"], entry["content"]),
                )
            app_logger.info("Seeded quizzes and learning module data.")

        existing = db.fetchone("SELECT id FROM commits LIMIT 1")
        if not existing:
            timestamp = datetime.now().isoformat()
            for branch, message, author in SAMPLE_COMMITS:
                db.execute(
                    "INSERT INTO commits (branch, message, author, timestamp) VALUES (?, ?, ?, ?)",
                    (branch, message, author, timestamp),
                )
            app_logger.info("Seeded commit history.")

        existing = db.fetchone("SELECT id FROM notifications LIMIT 1")
        if not existing:
            timestamp = datetime.now().isoformat()
            admin_user = db.fetchone("SELECT id FROM users WHERE username = ?", ("codeforge",))
            user_id = admin_user["id"] if admin_user else 1
            for title, message in SAMPLE_NOTIFICATIONS:
                db.execute(
                    "INSERT INTO notifications (title, message, user_id, created_at) VALUES (?, ?, ?, ?)",
                    (title, message, user_id, timestamp),
                )
            app_logger.info("Seeded notifications.")

        existing = db.fetchone("SELECT id FROM reviews LIMIT 1")
        if not existing:
            timestamp = datetime.now().isoformat()
            for title, status, reviewer, comments in SAMPLE_REVIEWS:
                db.execute(
                    "INSERT INTO reviews (title, status, reviewer, comments, created_at) VALUES (?, ?, ?, ?, ?)",
                    (title, status, reviewer, comments, timestamp),
                )
            app_logger.info("Seeded peer review records.")

        existing = db.fetchone("SELECT id FROM tests LIMIT 1")
        if not existing:
            timestamp = datetime.now().isoformat()
            for name, status, result, description in SAMPLE_TESTS:
                db.execute(
                    "INSERT INTO tests (name, status, result, description, created_at) VALUES (?, ?, ?, ?, ?)",
                    (name, status, result, description, timestamp),
                )
            app_logger.info("Seeded test records.")
    except Exception:
        app_logger.exception("Seed data generation failed.")
