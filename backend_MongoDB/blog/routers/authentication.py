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
DB = "MongoDB_Database"
MSG_COLLECTION = "authentication"
#Create User Route 
router = APIRouter(
    prefix="/authentication",
    tags=['Authentication']
)
#Functions
@router.get("/authentication" , tags=["Authentication"])
async def login():
    return {"login": "login"}

@router.post('/authentication')
async def register(user: models.User):
    #conn.local.user.insert_one(dict(user))
    return {"Register": "Register"}

@router.put('/authentication/{id}')
async def forgot_password(id,user: models.User):
    return {"forgot_password": "forgot_password"}

@router.delete('/authentication/{id}')
async def delete_account(id,user: models.User):
    return {"delete_account": "delete_account"}