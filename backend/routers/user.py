from fastapi import APIRouter, Depends
from .. import schemas, database
from sqlalchemy.orm import Session
from typing import List
from ..repository import userRepo


get_db = database.get_db
router = APIRouter(
    prefix="/user",
    tags=['users']
)

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return userRepo.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    return userRepo.show(id, db)