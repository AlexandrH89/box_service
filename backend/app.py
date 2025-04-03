from fastapi import FastAPI, Depends
from models import User as DBUser, get_db
from schemas import UserBase, User
from typing import List

from sqlalchemy.orm import Session

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/users/", response_model=User)
async def create_user(user: UserBase, db: Session = Depends(get_db)):
    db_user = DBUser(name=user.name, nickname=user.nickname, email=user.email)
    db.add(db_user)
    db.commit( )
    db.refresh(db_user)
    return db_user

@app.get("/users/", response_model=List[User])
async def get_user(db: Session = Depends(get_db)):
    users = db.query(DBUser).all()
    return users