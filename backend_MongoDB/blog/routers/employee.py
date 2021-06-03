from .. import models
from pymongo import MongoClient

import os
from fastapi import APIRouter, Depends,FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List


#Application Routes
"""
Our application has five routes:

POST / - creates a new student.
GET / - view a list of all students.
GET /{id} - view a single student.
PUT /{id} - update a student.
DELETE /{id} - delete a student.
"""
#Create Employee Route 

router = APIRouter(
    prefix="/employee",
    tags=['Employee']

)

# @app.get("/status" , tags=["Base Operations"])
# def get_status():
#     """Get status of messaging server."""
#     return {"status": "running"}


@router.get("/employee", response_model=List[str] , tags=["Employee"])
def get_channels():
    """Get all channels in list form."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        distinct_channel_list = msg_collection.distinct("Department")
        return distinct_channel_list


@router.get("/employee/{Department}", response_model=List[models.Message], tags=["Employee"])
def get_messages(Department: str):
    """Get all messages for the specified channel."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        msg_list = msg_collection.find({"Department":Department})
        response_msg_list = []
        for msg in msg_list:
            response_msg_list.append(models.Message(**msg))
        return response_msg_list

