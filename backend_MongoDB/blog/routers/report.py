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

#Connect to local database
DB = "Department_Report"
MSG_COLLECTION = "Department_level_Report"

#Create User Route 

router = APIRouter(
    prefix="/Report",
    tags=['Analysis Report']
)

@router.post("/Report", status_code=status.HTTP_201_CREATED , tags=["Analysis Report"])
async def post_report(message: models.Message):
    """Post a new message to the specified channel."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        result = msg_collection.insert_one(message.dict())
        ack = result.acknowledged
        return {"insertion": ack}

@router.delete("/Report", status_code=status.HTTP_201_CREATED , tags=["Analysis Report"],response_description="Delete a report")
async def delete_report(id: str):
    msg_collection = client[DB][MSG_COLLECTION]
    msg_list = msg_collection.find({"id":id})
    delete_result = msg_list.delete_one({"id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Report {id} not found")
