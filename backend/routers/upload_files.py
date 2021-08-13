from database import app,client
from fastapi import APIRouter
from fastapi import File, UploadFile

#Create User Route 
app = APIRouter()

db = client.files

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


