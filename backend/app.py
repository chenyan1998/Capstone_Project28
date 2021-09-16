from database import app
from routers import user

#Connect to MongoDB 
"""
Using the async motor driver to create our MongoDB client
and then we specify our database name college.
"""
app.include_router(user.app)