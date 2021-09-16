#!/bin/zsh

#This program test the backend.

export MONGODB_URL="mongodb+srv://Chenyan:Sutd30121998@cluster0.uxbcx.mongodb.net/db?retryWrites=true&w=majority"
pytest --html=report.html --self-contained-html
