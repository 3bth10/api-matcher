
from sqlalchemy.orm import Session
from models.resume import Resume


def get_resume(db: Session):
    resumes = db.query(Resume).all()
    return resumes


# def get_resume_by_id(id: int):
    
#     return {"resume": f"This is the resume with ID {id}."}

def create_resume(resume_data: dict, db: Session):
    if not resume_data:
        return {'err': 'data is not vaid!! '}
    resume = Resume(**resume_data)
    db.add(resume)
    db.commit()
    db.refresh
    return {"message": "Resume created successfully.", "resume": resume_data}

# def update_resume(resume_id: int, resume_data: Resume):
#     return {"message": f"Resume with ID {resume_id} updated successfully.", "resume": resume_data}

# def delete_resume(resume_id: int):
#     return {"message": f"Resume with ID {resume_id} deleted successfully."}