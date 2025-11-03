from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import uvicorn

from . import models, schemas
from .database import engine, get_db

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Portfolio API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Portfolio API", "version": "1.0.0"}

# Experience endpoints
@app.get("/api/experiences", response_model=List[schemas.Experience])
def read_experiences(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    experiences = db.query(models.Experience).order_by(models.Experience.id.desc()).offset(skip).limit(limit).all()
    return experiences

@app.post("/api/experiences", response_model=schemas.Experience)
def create_experience(experience: schemas.ExperienceCreate, db: Session = Depends(get_db)):
    db_experience = models.Experience(**experience.dict())
    db.add(db_experience)
    db.commit()
    db.refresh(db_experience)
    return db_experience

# Project endpoints
@app.get("/api/projects", response_model=List[schemas.Project])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    projects = db.query(models.Project).offset(skip).limit(limit).all()
    return projects

@app.post("/api/projects", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

# Skill endpoints
@app.get("/api/skills", response_model=List[schemas.Skill])
def read_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    skills = db.query(models.Skill).offset(skip).limit(limit).all()
    return skills

@app.post("/api/skills", response_model=schemas.Skill)
def create_skill(skill: schemas.SkillCreate, db: Session = Depends(get_db)):
    db_skill = models.Skill(**skill.dict())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

# Education endpoints
@app.get("/api/education", response_model=List[schemas.Education])
def read_education(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    education = db.query(models.Education).order_by(models.Education.graduation_date.desc()).offset(skip).limit(limit).all()
    return education

@app.post("/api/education", response_model=schemas.Education)
def create_education(education: schemas.EducationCreate, db: Session = Depends(get_db)):
    db_education = models.Education(**education.dict())
    db.add(db_education)
    db.commit()
    db.refresh(db_education)
    return db_education

# Contact form endpoint
@app.post("/api/contact", response_model=schemas.ContactMessage, status_code=201)
def create_contact_message(
    message: schemas.ContactMessageCreate, db: Session = Depends(get_db)
):
    db_message = models.ContactMessage(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

@app.get("/api/contact", response_model=List[schemas.ContactMessage])
def read_contact_messages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    messages = db.query(models.ContactMessage).order_by(models.ContactMessage.created_at.desc()).offset(skip).limit(limit).all()
    return messages

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
