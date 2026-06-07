
from fastapi import APIRouter, FastAPI
from  routes.users_router import router as users_router
from routes.resume import resume_router
from db import Base , engine
from models import users , resume , jobs


app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(users_router)
app.include_router(resume_router)



