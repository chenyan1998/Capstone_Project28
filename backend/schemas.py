from sqlalchemy.sql.elements import RollbackToSavepointClause
from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    name:str
    email:str
    password: str

class Employee(BaseModel):
    position: str
    risk: str

class SummaryMetric(BaseModel):
    title: str
    content: str

class ShowUser(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode = True 

class ShowEmployee(BaseModel):
    position: str
    risk: str
    class Config():
        orm_mode = True 

class ShowSummaryMetric(BaseModel):
    title: str
    content: str
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None