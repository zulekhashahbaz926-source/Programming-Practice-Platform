-- SQLite schema for Programming Practices Platform
-- This file can be executed to create the initial database structure.

PRAGMA foreign_keys = ON;

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_login DATETIME,
    is_admin INTEGER DEFAULT 0
);

-- Quizzes table (quiz metadata)
CREATE TABLE IF NOT EXISTS quizzes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    difficulty TEXT CHECK(difficulty IN ('Easy','Medium','Hard')),
    total_questions INTEGER NOT NULL,
    time_limit_seconds INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Quiz questions table
CREATE TABLE IF NOT EXISTS quiz_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quiz_id INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_option TEXT NOT NULL CHECK(correct_option IN ('A','B','C','D')),
    FOREIGN KEY (quiz_id) REFERENCES quizzes(id) ON DELETE CASCADE
);

-- Quiz results (user attempts)
CREATE TABLE IF NOT EXISTS quiz_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    quiz_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    taken_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (quiz_id) REFERENCES quizzes(id) ON DELETE CASCADE
);

-- Coding challenges table
CREATE TABLE IF NOT EXISTS coding_challenges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    difficulty TEXT CHECK(difficulty IN ('Beginner','Intermediate','Advanced')),
    starter_code TEXT,
    test_cases TEXT, -- JSON array of test case objects
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Challenge submissions (user attempts)
CREATE TABLE IF NOT EXISTS challenge_submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    challenge_id INTEGER NOT NULL,
    code TEXT NOT NULL,
    passed INTEGER NOT NULL CHECK(passed IN (0,1)),
    submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (challenge_id) REFERENCES coding_challenges(id) ON DELETE CASCADE
);

-- Leaderboard (aggregated scores)
CREATE TABLE IF NOT EXISTS leaderboard (
    user_id INTEGER PRIMARY KEY,
    total_score INTEGER NOT NULL,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Activity logs (generic event logging)
CREATE TABLE IF NOT EXISTS activity_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    activity_type TEXT NOT NULL,
    description TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);

-- Settings table (key‑value per user)
CREATE TABLE IF NOT EXISTS settings (
    user_id INTEGER NOT NULL,
    setting_key TEXT NOT NULL,
    setting_value TEXT,
    PRIMARY KEY (user_id, setting_key),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
