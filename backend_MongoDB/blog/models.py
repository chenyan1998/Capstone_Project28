from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

# Message class defined in Pydantic
class Message(BaseModel):
    Department: str
    Feedback: str
    Risk_Level: str

#Gentle information
class User(BaseModel):
    __tablename__ = 'users'
    id : str
    name : str
    email : str
    password :  str

class Employee(BaseModel):
    __tablename__ = 'employees'
    id : str
    position :  str
    risk : str
    individual_report :  str

class UserModel(BaseModel):
    id :  str
    name : str
    email : str
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
    email : str
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

