from database import app,client
from fastapi import APIRouter

#Create User Route 
app = APIRouter(
    # prefix="/BackendStatus",
    # tags=['BackendStatus']
)

@app.get("/BackendStatus" , tags=["BackendStatus"])
async def get_status():
    """Get status of server."""
    return {"status": "running"}

@app.post("/BackendStatus/details", tags=['BackendStatus'])
async def create_employee():
    
    return {"test "}

