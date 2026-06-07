
from fastapi import APIRouter , Depends
import services.users as user
from schemas.users import UserCreate
from db import get_db 
from sqlalchemy.orm import Session




router = APIRouter(prefix="/users", tags=["Users"])

@router.get('/')
def get_users(db : Session = Depends(get_db)):
    return user.get_users('',db)

@router.get('/{filter}')
def get_users(filter,db: Session = Depends(get_db)):
    return user.get_users(filter,db)
    

@router.post('/create')
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return user.create_user(user_data.dict() , db)

@router.put('/update/{user_id}')
def update_user(user_id: int, user_data: dict, db: Session = Depends(get_db)):
    return user.update_user(user_id, user_data, db)

@router.delete('/delete/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user.delete_user(user_id, db)