from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Depends
from app.database import Base, engine, get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import User, Task
from app.schemas import UserRead

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title="Task Manager", lifespan=lifespan)


@app.get("/users")
def getUsers(db: Session = Depends(get_db)):
    return db.scalars(select(User)).all()
    
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    pass