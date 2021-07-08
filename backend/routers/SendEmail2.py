from typing import List
from database import app,client
from models import EmailSchema
from fastapi import APIRouter
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig


SURVEY_URL = 'https://www.google.com/'

conf = ConnectionConfig(
    MAIL_USERNAME = "chenyan20210705@gmail.com",
    MAIL_PASSWORD = "oqlpkmymmiqwjuuw",
    MAIL_FROM = "chenyan20210705@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="Project 28",
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

app = APIRouter()

html = f"""
Hello, this is Project 28.
We are pleased to invite you to join our survey. Below is the survey link.
{SURVEY_URL}
Thank you.
"""
db = client.email2
# Q1 Haven't put any data to database 

@app.post("/emailtype2", response_description="Send email", tags=['Email2'])
async def simple_send(email: EmailSchema) -> JSONResponse:
    message = MessageSchema(
        subject="Project 28 Survey",
        recipients= email.dict().get("email"),  # List of recipients, as many as you can pass 
        body=html,
        )
    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})