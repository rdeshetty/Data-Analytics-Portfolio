from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Experience
class ExperienceBase(BaseModel):
    company: str
    position: str
    duration: str
    description: str
    is_current: bool = False

class ExperienceCreate(ExperienceBase):
    pass

class Experience(ExperienceBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Project
class ProjectBase(BaseModel):
    title: str
    description: str
    technologies: str
    github_url: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Skill
class SkillBase(BaseModel):
    name: str
    category: str
    proficiency: int

class SkillCreate(SkillBase):
    pass

class Skill(SkillBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Education
class EducationBase(BaseModel):
    institution: str
    degree: str
    field_of_study: str
    gpa: str
    graduation_date: str
    location: str

class EducationCreate(EducationBase):
    pass

class Education(EducationBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Contact
class ContactMessageBase(BaseModel):
    name: str
    email: EmailStr
    message: str

class ContactMessageCreate(ContactMessageBase):
    pass

class ContactMessage(ContactMessageBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
