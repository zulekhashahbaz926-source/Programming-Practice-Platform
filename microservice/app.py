from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database.db_manager import DatabaseManager

app = FastAPI(
    title="Zyntriva Microservice",
    description="A small microservice exposing module and version control data for the Zyntriva platform.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

db = DatabaseManager()

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "Zyntriva Microservice"}

@app.get("/modules")
def list_learning_modules():
    quizzes = db.fetchall("SELECT id, title, description, category, content FROM quizzes ORDER BY id")
    return [dict(row) for row in quizzes]

@app.get("/commits")
def get_commit_history():
    commits = db.get_commits()
    return [dict(row) for row in commits]

@app.get("/users/{username}")
def get_user_profile(username: str):
    user = db.find_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = dict(user)
    user_data.pop("password", None)
    return user_data
