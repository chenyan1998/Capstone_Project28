from database import app
from routers import user,backendstatus,employee,report,surveyemployee,sendemail,upload_files
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081" ,
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
app.include_router(sendemail.app)
app.include_router(upload_files.app)


