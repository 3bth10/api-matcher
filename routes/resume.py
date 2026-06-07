from fastapi import APIRouter, Depends
import  services.resume as  resume
from schemas.resume import Resume
from sqlalchemy.orm import Session
from db import get_db

resume_router = APIRouter(prefix="/resume", tags=["Resume"])

@resume_router.get('/')
def get_resume(db: Session = Depends(get_db)):
    return resume.get_resume(db)

@resume_router.post('/create')
def create_resume(resume_data: dict, db: Session = Depends(get_db)):
    return resume.create_resume(resume_data, db)

@resume_router.get('/{id}')
def get_resume_by_id(id: int):
    return resume.get_resume_by_id(id)

@resume_router.put('/update/{id}')
def update_resume(id: int, resume_data: Resume):
    return resume.update_resume(id, resume_data)

@resume_router.delete('/delete/{id}')
def delete_resume(id: int):
    return resume.delete_resume(id)