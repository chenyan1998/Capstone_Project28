export DEBUG_MODE=True
export DB_URL="mongodb+srv://Chenyan:Sutd30121998@cluster0.uxbcx.mongodb.net/db?retryWrites=true&w=majority"

export DB_NAME="farmstack"

export JWT_SECRET_KEY="Sutd30121998301219983012199830121998"

export REALM_APP_ID="application-0-svsqj"

uvicorn main:app --reload

