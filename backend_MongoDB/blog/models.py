from sqlalchemy.sql.sqltypes import String
from pydantic import BaseModel
from typing import Optional, List
from bson import ObjectId

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
    individual_report = String

class UserModel(BaseModel):
    id= String
    name= String
    email= String
    password: Optional[str]
    

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "password": "307896",
            }
        }

class UpdateUsertModel(BaseModel):
    name: Optional[str]
    email= String
    password: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "password": "307896",
            }
        }

