from .. import models
from pymongo import MongoClient
import os
from fastapi import APIRouter, Depends,FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List

#Connect to local database
DB = "MongoDB_Database"
MSG_COLLECTION = "report"

#Create User Route 
router = APIRouter(
    prefix="/Report",
    tags=['Analysis Report']
)
#Functions

@router.get("/sumarydynamixcharts" )
async def summary_chart_list():
    return {"chart list": "chart list"}

@router.get("/sumarydynamixcharts/{metrics}" )
async def get_chart_metrics():
    return {"chart": "chart type"}

@router.get("/sumarydynamixcharts/{metrics}/age" )
async def charts_filter_Age():
    return {"chart age": "chart age"}

@router.get("/sumarydynamixcharts/{metrics}/years" )
async def charts_filter_years():
    return {"chart years": "chart years"}

@router.get("/sumarydynamixcharts/{metrics}/department" )
async def charts_filter_department():
    return {"chart department": "chart department"}

@router.put("/Report", status_code=status.HTTP_201_CREATED , tags=["Analysis Report"])
async def update_charts_report(message: models.Message):
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        result = msg_collection.insert_one(message.dict())
        ack = result.acknowledged
        return {"insertion": ack}

@router.delete("/sumarydynamixcharts/{metrics}", status_code=status.HTTP_201_CREATED , tags=["Analysis Report"],response_description="Delete a report")
async def delete_chart_report(id: str):
    msg_collection = client[DB][MSG_COLLECTION]
    msg_list = msg_collection.find({"id":id})
    delete_result = msg_list.delete_one({"id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Report {id} not found")

@router.get("/sumarydynamixtables" )
async def summary_table_table():
    return {"tables list": "tables list"}

@router.get("/sumarydynamixtables/{metrics}" )
async def get_table_metrics():
    return {"tables": "tables type"}

@router.get("/sumarydynamixtables/{metrics}/age" )
async def tables_filter_Age():
    return {"tables age": "tables age"}

@router.get("/sumarydynamixtables/{metrics}/years" )
async def tables_filter_years():
    return {"tables years": "tables years"}

@router.get("/sumarydynamixtables/{metrics}/department" )
async def tables_filter_department():
    return {"tables department": "tables department"}


@router.put("/Table", status_code=status.HTTP_201_CREATED , tags=["Analysis Report"])
async def update_table_report(message: models.Message):
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        result = msg_collection.insert_one(message.dict())
        ack = result.acknowledged
        return {"insertion": ack}

@router.delete("/sumarydynamixtables/{metrics}", status_code=status.HTTP_201_CREATED , tags=["Analysis Report"],response_description="Delete a report")
async def delete_table_report(id: str):
    msg_collection = client[DB][MSG_COLLECTION]
    msg_list = msg_collection.find({"id":id})
    delete_result = msg_list.delete_one({"id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Report {id} not found")
