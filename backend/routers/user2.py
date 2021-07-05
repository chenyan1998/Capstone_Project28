from database import app,client
from typing import Optional, List

#Create User Route 
app = APIRouter(

)

db = client.college

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
    
