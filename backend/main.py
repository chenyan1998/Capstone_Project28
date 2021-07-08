from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List
from database import client,app
import motor.motor_asyncio
import os
from routers import user,backendstatus,employee,report,surveyemployee,SendEmail2

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(backendstatus.app)
app.include_router(employee.app)
app.include_router(user.app)
app.include_router(report.app)
app.include_router(surveyemployee.app)
app.include_router(SendEmail2.app)
