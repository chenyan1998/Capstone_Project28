from sqlalchemy.sql.sqltypes import String
from pydantic import BaseModel

# Message class defined in Pydantic
class Message(BaseModel):
    Department: str
    Feedback: str
    Risk_Level: str

class User(BaseModel):
    __tablename__ = 'users'
    id = String
    name = String
    email = String
    password = String 

class Employee(BaseModel):
    __tablename__ = 'employees'
    id = String
    position = String
    risk = String