from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class UserBase(BaseModel):
    username: str
    email: str

class UserSchema(UserBase):
    id: int

class User:
    def __init__(self, id: int, username: str, email: str):
        self.id = id
        self.username = username
        self.email = email

users = [
    User(id=0, username="great-username", email="averageemail@mail.dot"),
    User(id=1, username="amazingname", email="serious@professional.mail"),
    User(id=2, username="username", email="e@ma.il")
]

@app.get('/users', response_model=List[UserSchema])
async def get_users():
    return users

@app.get('/users/{user_id}', response_model=UserSchema)
async def get_user(user_id: int):
    current_user = ''
    for user in users:
        if user.id == user_id:
            current_user = user
            break
    
    if current_user:
        return current_user
    else:
        raise HTTPException(404, "No user with such id found")

@app.post('/create_user', response_model=UserSchema)
async def create_user(user_data: UserBase):
    user = User(id=len(users), **user_data.dict())
    users.append(user)
    return user