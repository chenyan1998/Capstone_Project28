from models import ReportModel,IndividualReportModel
from database import app,client
from fastapi import APIRouter,Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

#Create User Route 
app = APIRouter(
)

db = client.report
#db is a database , the database we used is called report 

#Create report route 
#Report list , to check who already take this 
@app.post("/report", response_description="Add new report", response_model=ReportModel,tags=['Report'])
async def create_report(report: ReportModel = Body(...)):
    report = jsonable_encoder(report)
    new_report = await db["report"].insert_one(report)
    created_report = await db["report"].find_one({"_id": new_report.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_report)

@app.post("/report/individual", response_description="Add new report", response_model=IndividualReportModel,tags=['Report'])
async def create_report(report: IndividualReportModel = Body(...)):
    report = jsonable_encoder(report)
    new_report = await db["RF_Summary_Report"].insert_one(report)
    created_report = await db["RF_Summary_Report"].find_one({"_id": new_report.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_report)

@app.get(
    "/report/individuals", response_description="List all individual report", response_model=List[IndividualReportModel],tags=['Report']
)
async def list_individual_report():
    report= await db["RF_Summary_Report"].find().to_list(1000)
    return report

@app.get("/report/individuals/{employee_id}", response_model=List[IndividualReportModel], tags=['Report'])
async def get_individuals_report(employee_id: int):
    report= await db["RF_Summary_Report"].find({'Employee_id': employee_id}).to_list(1000)
    return report

@app.get("/report/individuals/year/{year}", response_model=List[IndividualReportModel], tags=['Report'])
async def get_individuals_report_by_year(year: str):
    report= await db["RF_Summary_Report"].find({'year': year}).to_list(1000)
    return report

@app.post("/report", response_description="Update report", response_model=ReportModel,tags=['Report'])
async def update_report(id: str, data_x:str,data_y:str):
    db["report"].update_one({
        "_id":id
    },{
        "$set":{'data_x':data_x,
                'data_y':data_y
        }
    },upsert=False,multi=False)

@app.get(
    "/report", response_description="List all report", response_model=List[ReportModel],tags=['Report']
)
async def list_report():
    report= await db["report"].find().to_list(1000)
    return report

@app.get("/report/{metric}", response_model=List[ReportModel], tags=['Report'])
async def get_report_metric(metric: str):
    report= await db["report"].find({'metric': metric}).to_list(1000)
    return report
   
@app.get("/report/list_table", response_model=List[ReportModel], tags=['Report'])
async def summary_table_list():
    report= await db["report"].find({'name':"report"}).to_list(1000)
    return report

@app.delete("/report/{id}", response_description="Delete a report",tags=['Report'])
async def delete_report(id: str):
    delete_report = await db["report"].delete_one({"_id": id})

    if delete_report.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Report {id} not found")
