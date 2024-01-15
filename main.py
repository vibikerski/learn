from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import crud as db

app = FastAPI()

class UserBase(BaseModel):
    username: str
    email: str

class UserSchema(UserBase):
    id: int

@app.get('/users', response_model=List[UserSchema])
async def get_users():
    try:
        return db.get_all_users(db.cursor)
    except:
        raise HTTPException(500, "Internal server error")


@app.get('/users/{user_id}', response_model=UserSchema)
async def get_user(user_id: int):
    try:
        return db.get_user(db.cursor, user_id)
    except:
        raise HTTPException(500, "Internal server error")


@app.post('/create_user', response_model=UserSchema)
async def create_user(user_data: UserBase):
    try:
        return db.add_user(db.con, db.cursor, **dict(user_data))
    except:
        raise HTTPException(500, "Internal server error")