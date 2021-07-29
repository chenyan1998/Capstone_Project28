from database import app,client
from fastapi import APIRouter

#Create User Route 
app = APIRouter(
)

@app.get("/BackendStatus" , tags=["BackendStatus"])
async def get_status():
    """Get status of server."""
    return {"status": "running"}
