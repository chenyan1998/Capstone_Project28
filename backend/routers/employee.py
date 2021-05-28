from fastapi import APIRouter, Depends
from .. import schemas, database, models 
from ..utils import oauth2
from sqlalchemy.orm import Session
from typing import List
from ..repository import employeeRepo
get_db = database.get_db
router = APIRouter(
    prefix="/employee",
    tags=['employees']

)

@router.get('/', response_model=List[schemas.ShowEmployee])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return employeeRepo.get_all(db)

# @router.get('/', response_model=List[schemas.ShowEmployee])
# def all(db: Session = Depends(get_db)):
#     return employeeRepo.get_all(db)

@router.post('/', status_code=201)
def create(request: schemas.Employee, db: Session = Depends(get_db)):
    return employeeRepo.create(request, db)

@router.delete('/{id}', status_code=204)
def destroy(id, db:Session = Depends(get_db)):
    return employeeRepo.destroy(id, db)

@router.put('/{id}', status_code=202)
def update(id, request: schemas.Employee, db: Session = Depends(get_db)):
    return employeeRepo.update(id, request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowEmployee)
def show(id, db: Session = Depends(get_db)):
    return employeeRepo.show(id, db)

