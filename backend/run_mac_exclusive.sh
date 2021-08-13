#!/bin/zsh

#This program run the backend

export MONGODB_URL="mongodb+srv://Chenyan:Sutd30121998@cluster0.uxbcx.mongodb.net/db?retryWrites=true&w=majority"
uvicorn main:app --reload


