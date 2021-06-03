# A Bare Bones Slack API
# Illustrates basic usage of FastAPI w/ MongoDB
from backend.models import User
from pymongo import MongoClient
from . import models
import os
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List


DB = "Department_Report"
MSG_COLLECTION = "Department_level_Report"


# Instantiate the FastAPI
app = FastAPI()
# Step1 : Connect to MongoDB 
# client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
# db = client.college
# We're using the async motor driver to create our MongoDB client, and then we specify our database name college.

@app.get("/status" , tags=["Base Operations"])
def get_status():
    """Get status of messaging server."""
    return {"status": "running"}


@app.get("/Department", response_model=List[str] , tags=["Employee"])
def get_channels():
    """Get all channels in list form."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        distinct_channel_list = msg_collection.distinct("Department")
        return distinct_channel_list


@app.get("/Department/{Department}", response_model=List[models.Message], tags=["Employee"])
def get_messages(Department: str):
    """Get all messages for the specified channel."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        msg_list = msg_collection.find({"Department":Department})
        response_msg_list = []
        for msg in msg_list:
            response_msg_list.append(models.Message(**msg))
        return response_msg_list


@app.get("/user", response_model=List[models.Message], tags=["User"])
def get_messages(id: str):
    """Get all messages for the specified channel."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        msg_list = msg_collection.find({"id":id})
        response_msg_list = []
        for msg in msg_list:
            response_msg_list.append(models.User(**msg))
        return response_msg_list

@app.post("/user", status_code=status.HTTP_201_CREATED , tags=["User"])
def post_report(user: models.User):
    """Post a new user """
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        result = msg_collection.insert_one(user.dict())
        ack = result.acknowledged
        return {"insertion": ack}

@app.delete("/{user}", status_code=status.HTTP_201_CREATED , tags=["User"],response_description="Delete a user")
async def delete_user(id: str):
    msg_collection = client[DB][MSG_COLLECTION]
    msg_list = msg_collection.find({"id":id})
    delete_result = msg_list.delete_one({"id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"User {id} not found")

# @app.put("/{id}", response_description="Update a user", response_model=models.UpdateUsertModel)
# async def update_user(id: str, user: User = Body(...)):
#     user = {k: v for k, v in user.dict().items() if v is not None}

#     if user(user) >= 1:
#         msg_collection = client[DB][MSG_COLLECTION]
#         msg_list = msg_collection.find({"id":id})
#         update_result = msg_list.update_one({"id": id}, {"$set": user})

#         if update_result.modified_count == 1:
#             if (
#                 updated_user := msg_list.find_one({"id": id})
#             ) is not None:
#                 return updated_user

#     if (existing_user := msg_list.find_one({"id": id})) is not None:
#         return existing_user

#     raise HTTPException(status_code=404, detail=f"User {id} not found")


@app.post("/Report", status_code=status.HTTP_201_CREATED , tags=["Analysis Report"])
def post_report(message: models.Message):
    """Post a new message to the specified channel."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        result = msg_collection.insert_one(message.dict())
        ack = result.acknowledged
        return {"insertion": ack}

@app.delete("/Report", status_code=status.HTTP_201_CREATED , tags=["Analysis Report"],response_description="Delete a report")
async def delete_report(id: str):
    msg_collection = client[DB][MSG_COLLECTION]
    msg_list = msg_collection.find({"id":id})
    delete_result = msg_list.delete_one({"id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Report {id} not found")

