import sqlite3
import os
import bcrypt

# Path to SQLite database file (placed in project root)
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "app.db")

def get_connection():
    """Create a new SQLite connection.
    Returns:
        sqlite3.Connection: Database connection object.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database using the SQL schema file.
    This function reads `backend/init_db.sql` and executes it.
    It is idempotent – tables are created only if they do not exist.
    """
    schema_path = os.path.join(os.path.dirname(__file__), "init_db.sql")
    if not os.path.exists(schema_path):
        raise FileNotFoundError(f"Schema file not found: {schema_path}")
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()
    conn = get_connection()
    try:
        conn.executescript(schema_sql)
        conn.commit()
    finally:
        conn.close()

def hash_password(plain_password: str) -> str:
    """Hash a plaintext password using bcrypt.
    Returns the hashed password as a UTF‑8 string.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain_password.encode("utf-8"), salt)
    return hashed.decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plaintext password against a stored bcrypt hash.
    """
    try:
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
    except Exception:
        return False

def get_user_by_email(email: str):
    """Fetch a user record by email.
    Returns a tuple matching the columns defined in the `users` table or ``None``.
    """
    conn = get_connection()
    try:
        cur = conn.execute("SELECT * FROM users WHERE email = ?", (email,))
        return cur.fetchone()
    finally:
        conn.close()

def create_user(name: str, email: str, password: str):
    """Create a new user entry.
    The password will be stored as a bcrypt hash.
    """
    hashed = hash_password(password)
    conn = get_connection()
    try:
        conn.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (name, email, hashed),
        )
        conn.commit()
    finally:
        conn.close()
