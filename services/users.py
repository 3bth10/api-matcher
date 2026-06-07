import bcrypt
from models.users import Users
from sqlalchemy.orm import Session 
from sqlalchemy import extract

def get_users(data: None , db: Session):
    if data :
        data = int(data)
        if data <= 12:
            return 'This is a month'
           # return db.query(Users).filter(extract('month',Users.create_at)== '6').all()
        if data > 2000:
            return 'This is a year'
            #return db.query(Users).filter(extract('month',Users.create_at)== '6').all()
    return db.query(Users).all()

def create_user(data: dict, db: Session):
    if not data.get("username") or not data.get("password"):
        return {"message": "Username and password are required."}
    hashed_password = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt())

    user = Users(username=data["username"], hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "User created successfully.", "user": user}

def update_user(user_id: int, data: dict, db: Session):
    user = db.query(Users).filter(Users.id == user_id).first()
    if not user:
        return {"message": "User not found."}
    
    if data.get("username"):
        user.username = data["username"]
    if data.get("role"):
        user.role = data["role"]
    if data.get("create_at"):
        user.create_at = data["create_at"]
    if data.get("password"):
        user.hashed_password = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt())
    db.commit()
    db.refresh(user)

    return {"message": "User updated successfully.", "user": user}

def delete_user(user_id: int , db: Session):
    user = db.query(Users).filter(Users.id == user_id).first()
    if not user:
        return {"message": "User not found."}
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully."}