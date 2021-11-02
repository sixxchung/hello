from fastapi import APIRouter 
from typing import List

import sys, os
#sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append('/Users/onesixx/my/git/hello/app')

from database.conn import session
from database.model import UserTable, User

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
def update_users(userList: List[User]):
    #print("-=======>Sixx")
    #print(users)
    for i in userList:
        user = session.query(UserTable).filter(UserTable.id == i.id).first()
        print("-=======>Sixx")
        print(i.age)
        user.name= i.name
        user.age = i.age
        session.commit()

    return f"{userList[0].name} updated..."

@router.delete("/users/{user_id}")
def delete_users(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).delete()
    session.commit()

    return  "delete..."



