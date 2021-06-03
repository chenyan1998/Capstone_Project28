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
    prefix="/BackendStatus",
    tags=['BackendStatus']
)

@router.get("/BackendStatus" , tags=["BackendStatus"])
async def get_status():
    """Get status of server."""
    return {"status": "running"}