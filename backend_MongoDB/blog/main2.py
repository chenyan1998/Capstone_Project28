# A Bare Bones Slack API
# Illustrates basic usage of FastAPI w/ MongoDB
from pymongo import MongoClient
from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List

DB = "Department_Report"
MSG_COLLECTION = "Department_level_Report"


# Message class defined in Pydantic
class Message(BaseModel):
    Department: str
    Feedback: str
    Risk_Level: str


# Instantiate the FastAPI
app = FastAPI()


@app.get("/status")
def get_status():
    """Get status of messaging server."""
    return {"status": "running"}


@app.get("/Department", response_model=List[str])
def get_channels():
    """Get all channels in list form."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        distinct_channel_list = msg_collection.distinct("Department")
        return distinct_channel_list


@app.get("/Department/{Department}", response_model=List[Message])
def get_messages(Department: str):
    """Get all messages for the specified channel."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        msg_list = msg_collection.find({"Department":Department})
        response_msg_list = []
        for msg in msg_list:
            response_msg_list.append(Message(**msg))
        return response_msg_list


@app.post("/post_report", status_code=status.HTTP_201_CREATED)
def post_report(message: Message):
    """Post a new message to the specified channel."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        result = msg_collection.insert_one(message.dict())
        ack = result.acknowledged
        return {"insertion": ack}
