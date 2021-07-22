from models import rate
from typing import Counter, List
from database import app,client
from models import SurveyEmployeeModel

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import APIRouter,Body, HTTPException, status


#Create User Route 
app = APIRouter(
    # prefix="/BackendStatus",
    # tags=['BackendStatus']
)

db = client.email 
collection=["email"]

#Create employee route 
#Survey Employee list , to check who haven't fill the survey 
@app.post("/email/post_rate", response_description="rate", response_model= rate,tags=['Email'])
async def post_rate(b: rate = Body(...)):
    b = jsonable_encoder(b)
    await db["count"].insert_one(b)
    return JSONResponse(status_code=status.HTTP_201_CREATED)

@app.get(
    "/email/completion_rate", response_description="Return the survey completion rate",tags=['Email']
)
async def get_survery_completion_rate():
    all_employee = 300
    surveyemployees = await client.Survey["Survey1"].find().to_list(1000)
    completion_rate=len(surveyemployees)/all_employee
    #student = {k: v for k, v in surveyemployees.dict().items() if v is not None}
    return completion_rate


@app.post("/email", response_description="Individual Employee does not finish survey", response_model= SurveyEmployeeModel,tags=['Email'])
async def create_survey_employee(surveyemployee: SurveyEmployeeModel = Body(...)):
    surveyemployee = jsonable_encoder(surveyemployee)
    new_surveyemployee = await db["email"].insert_one(surveyemployee)
    created_surveyemployee = await db["email"].find_one({"_id": new_surveyemployee.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_surveyemployee)


@app.get(
    "/email", response_description="List all employees that they does not finish survey", response_model=List[SurveyEmployeeModel],tags=['Email']
)
async def list_surveyemployees():
    surveyemployees= await db["email"].find().to_list(1000)
    return surveyemployees

@app.get(
    "/email/{id}", response_description="Get a single employee that he does not finish survey ", response_model=SurveyEmployeeModel,tags=['Email']
)
async def show_surveyemployee(id: str):
    if (surveyemployee := await db["email"].find_one({"_id": id})) is not None:
        return surveyemployee

    raise HTTPException(status_code=404, detail=f"user {id} not found")


print(" Finished ! ")
    
