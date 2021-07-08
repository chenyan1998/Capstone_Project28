from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List
from schemas import PyObjectId

class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    department: str = Field(...)
    number_employee: float = Field(..., le=100.0)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "department": "IT",
                "number_employee": "11.0",
            }
        }

class SurveyEmployeeModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    department: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "department": "IT",
            }
        }

class EmailSchema(BaseModel):
    email: List[EmailStr]

class UpdateUserModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    department: Optional[str]
    number_employee: Optional[float]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "department": "IT",
                "number_employee": "11.0",
            }
        }


class EmployeeModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    department: str = Field(...)
    employee_details: str = Field(...)
    employee_risk_level: float = Field(..., le=10.0)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "department": "IT",
                "employee_details": "details",
                "employee_risk_level":"3.0",
            }
        }


class UpdateEmployeeModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    department: Optional[str]
    employee_details: Optional[str]
    employee_risk_level: Optional[float]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "department" : "IT",
                "employee_details": "details",
                "employee_risk_level":"3.0",
            }
        }

class ReportModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    metric: str = Field(...)
    department: str = Field(...)
    year: str = Field(...)
    report_format: str = Field(...)
    question: str = Field(...)
    label_x: str= Field(...)
    label_y: str= Field(...)
    data_x: Optional[List[str]] = Field(...)
    data_y: Optional[List[str]] = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "metric": "wellbeing, coreValues, personality or opinion",
                "department": "HR or Logistics",
                "year": "2021",
                "question": "1 or 2 or 3",
                "report_format":"table or chart",
                "label_x": "month or employee_id",
                "label_y": "EEI Score",
                "data_x": [1,2,3],
                "data_y": [20,30,40]
            }
        }
class IndividualReportModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    Employee_id: str = Field(...)
    EES_score: str= Field(...)
    Opinion: str= Field(...)
    Wellbeing: str = Field(...)
    Core_values: str = Field(...)
    Personality: str = Field(...)    
    Flight_risk_label: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "Employee_id": "1000023",
                "EES_score": "91",
                "Opinion": "97",
                "Wellbeing": "89",
                "Core_values": "85",
                "Personality":"99",
                "Flight_risk_label":"1:High"
            }
        }



class EmailSchema(BaseModel):
    email: List[EmailStr]
    
# class Surveyresult(BaseModel):
#     id: str = Field(...)
#     age: str= Field(...)
#     Year: str= Field(...)
#     department: str= Field(...)
#     wellbeing: str= Field(...)
#     core_values: str= Field(...)
#     personality: str= Field(...)
#     opinion: str= Field(...)

#     class Config:
#         allow_population_by_field_name = True
#         arbitrary_types_allowed = True
#         json_encoders = {ObjectId: str}
#         schema_extra = {
#             "example": {
#                 "name": "Jane Doe",
#                 "metric": "dynamic metric",
#                 "filter_type": "Age,Years,Departments",
#                 "report_format":"Tables or charts ",
#             }
#         }