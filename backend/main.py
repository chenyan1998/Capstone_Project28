from database import app
import os
from routers import user,backendstatus,employee,report, sendemail
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

app.include_router(backendstatus.router)
app.include_router(employee.app)
app.include_router(user.app)
app.include_router(report.app)
app.include_router(sendemail.app)

@app.get("/hello")
async def read_main():
    return {"msg": "Hello World"}
