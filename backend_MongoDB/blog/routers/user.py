from .. import models
from pymongo import MongoClient
from .. import schemas
from .. import config
import os
from fastapi import APIRouter, Depends, FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List

#Connect to local database
DB = "Department_Report"
MSG_COLLECTION = "Department_level_Report"

#Application Routes
"""
Our application has five routes:

POST / - creates a new student.
GET / - view a list of all students.
GET /{id} - view a single student.
PUT /{id} - update a student.
DELETE /{id} - delete a student.
"""
#Create User Route 
router = APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.get("/user/t1", response_model=List[models.Message], tags=["Users"])
async def find_all_users():
    return schemas.serializeList(config.db.cnn.local.user.find())

@router.get("/user", response_model=List[models.Message], tags=["Users"])
async def get_messages(id: str):
    """Get all messages for the specified channel."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        msg_list = msg_collection.find({"id":id})
        response_msg_list = []
        for msg in msg_list:
            response_msg_list.append(models.User(**msg))
        return response_msg_list

@router.post("/user", status_code=status.HTTP_201_CREATED , tags=["Users"])
async def post_report(user: models.User):
    """Post a new user """
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        result = msg_collection.insert_one(user.dict())
        ack = result.acknowledged
        return {"insertion": ack}

@router.delete("/{user}", status_code=status.HTTP_201_CREATED , tags=["Users"],response_description="Delete a user")
async def delete_user(id: str):
    msg_collection = client[DB][MSG_COLLECTION]
    msg_list = msg_collection.find({"id":id})
    delete_result = msg_list.delete_one({"id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"User {id} not found")