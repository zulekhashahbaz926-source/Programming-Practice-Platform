-- init_db.sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    level TEXT DEFAULT 'Beginner',
    points INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    difficulty TEXT NOT NULL,
    question_text TEXT NOT NULL,
    answer TEXT NOT NULL,
    hint TEXT
);

CREATE TABLE IF NOT EXISTS progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    status TEXT NOT NULL, -- solved / attempted
    score INTEGER,
    date TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(question_id) REFERENCES questions(id)
);

CREATE TABLE IF NOT EXISTS test_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    test_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    score INTEGER,
    time_taken REAL,
    date TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
