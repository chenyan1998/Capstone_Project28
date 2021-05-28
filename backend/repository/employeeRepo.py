from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException
def get_all(db: Session):
    employees = db.query(models.Employee).all()
    return employees

def create(request: schemas.Employee, db: Session):
    new_employee = models.Employee(position=request.position, risk=request.risk)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def destroy(id:int, db: Session):
    employee = db.query(models.Employee).filter(models.Employee.id==id)
    if not employee.first():
        raise HTTPException(status_code=404, detail=f'Employee with id {id} not found')
    employee.delete(synchronize_session=False)
    db.commit()
    return {'done'}

def update(id:int, request:schemas, db: Session):
    employee = db.query(models.Employee).filter(models.Employee.id == id)
    if not employee.first():
        raise HTTPException(status_code=404, detail=f'Employee with id {id} not found')
    employee.update(request)
    db.commit()
    return 'update'

def show(id:int, db: Session):
    employee = db.query(models.Employee).filter(models.Employee.id == id).first()
    if not employee:
        raise HTTPException(status_code=404, detail = f'Employee with the {id} is not available')
    return employee
