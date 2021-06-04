# A Bare Bones Slack API
# Illustrates basic usage of FastAPI w/ MongoDB
from pymongo import MongoClient
from . import models
import os
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List
from .routers import authentication, user, employee , report , BackendStatus


DB = "Department_Report"
MSG_COLLECTION = "Department_level_Report"


# Instantiate the FastAPI
app = FastAPI()
# Step1 : Connect to MongoDB 
# client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
# db = client.college
# We're using the async motor driver to create our MongoDB client, and then we specify our database name college.
app.include_router(BackendStatus.router)
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(employee.router)
app.include_router(report.router)


