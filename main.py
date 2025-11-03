from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
import os
from pathlib import Path

app = FastAPI(title="Portfolio API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
BASE_DIR = Path(__file__).parent
DATABASE_URL = os.path.join(BASE_DIR, "portfolio.db")

def get_db_connection():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS experiences (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT NOT NULL,
        position TEXT NOT NULL,
        duration TEXT NOT NULL,
        description TEXT NOT NULL,
        is_current BOOLEAN DEFAULT FALSE
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        technologies TEXT NOT NULL,
        github_url TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        proficiency INTEGER NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contact_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

# Models
class Experience(BaseModel):
    company: str
    position: str
    duration: str
    description: str
    is_current: bool = False

class Project(BaseModel):
    title: str
    description: str
    technologies: str
    github_url: Optional[str] = None

class Skill(BaseModel):
    name: str
    category: str
    proficiency: int

class ContactMessage(BaseModel):
    name: str
    email: str
    message: str

# Routes
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Portfolio API"}

@app.get("/api/experiences", response_model=List[dict])
async def get_experiences():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM experiences ORDER BY id DESC")
    experiences = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return experiences

@app.get("/api/projects", response_model=List[dict])
async def get_projects():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    projects = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return projects

@app.get("/api/skills", response_model=List[dict])
async def get_skills():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM skills")
    skills = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return skills

@app.post("/api/contact", status_code=201)
async def create_contact_message(message: ContactMessage):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contact_messages (name, email, message) VALUES (?, ?, ?)",
        (message.name, message.email, message.message)
    )
    conn.commit()
    conn.close()
    return {"message": "Message sent successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)