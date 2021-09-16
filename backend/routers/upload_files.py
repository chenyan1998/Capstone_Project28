from database import app,client
from fastapi import APIRouter
from fastapi import File, UploadFile


#Create User Route 
app = APIRouter()

db = client.files

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    # dst = '/Users/chenyan/Documents/GitHub/Capstone_Project28/model'
    # shutil.copy2(file, dst)
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    file1 = open('/Users/chenyan/Documents/GitHub/Capstone_Project28/model/data_temp2.csv',"w") 
    # for i in file:
    #     file1.writelines("{}\n".format(i))    
    # file1.close()
    # dst = '/Users/chenyan/Documents/GitHub/Capstone_Project28/model'
    # shutil.copy2(file, dst)
    with open(file, "wb") as buffer:
        shutil.copyfileobj(file1, buffer)
    return {"filename": file.filename}

