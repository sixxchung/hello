
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db import Base
from db import ENGINE

class UserTable(Base):
    __tablename__ = 'user'
    id  = Column(Integer, primary_key=True,  autoincrement=True)
    name= Column(String(50))# , nullable=False)
    age = Column(Integer)

class User(BaseModel):
    id : int
    name : str
    age : int

# SELECT user.id AS user_id, user.name AS user_name, user.age AS user_age 
# FROM user