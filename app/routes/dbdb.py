from fastapi import APIRouter 
from typing import List

from db import session
from model import UserTable, User

import requests
from starlette.requests import Request
from starlette.responses import JSONResponse

router = APIRouter()

@router.get("/")
def read_users():
    return JSONResponse(
        {'hello':'sixxx'}
    )


@router.get("/users")
async def read_users():
    print("-=======>Sixx")
    users = session.query(UserTable).all()
    return users

@router.get("/users/{user_id}")
def read_users(user_id: int):
    user= session.query(UserTable).filter(UserTable.id==user_id).first()
    return user

@router.post("/users")
def create_users(name:str, age:int):
    user= UserTable()
    user.name = name
    user.age = age
    session.add(user)
    session.commit()
    return f"{name} created."

@router.put("/users")
def update_users(users: List[User]):
    for i in users:
        user = session.query(UserTable).filter(UserTable.id == i.id).first()
        user.name= i.name
        user.age = i.age
        return users
    return f"{user[0].name} updated..."

@router.delete("/users/{user_id}")
def delete_users(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).delete()
    session.commit()

    return  f"{user[0].name} delete..."



