from fastapi import FastAPI
import motor.motor_asyncio
import os

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])