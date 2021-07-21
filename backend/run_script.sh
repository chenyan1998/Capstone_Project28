#!/bin/zsh

#This program run the backend

# export DEBUG_MODE=True
export MONGODB_URL="mongodb+srv://Chenyan:Sutd30121998@cluster0.uxbcx.mongodb.net/db?retryWrites=true&w=majority"
# export DB_NAME="farmstack"
# export JWT_SECRET_KEY="Sutd30121998301219983012199830121998"
# export REALM_APP_ID="application-0-svsqj"
uvicorn main:app --reload

# Install the requirements:
pip install -r requirements.txt

# Configure the location of your MongoDB database:
export MONGODB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"

# Start the service:
uvicorn main:app --reload
