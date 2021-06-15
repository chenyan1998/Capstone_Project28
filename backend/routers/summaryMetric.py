from fastapi import APIRouter, Depends
from .. import schemas, database 
from ..utils import oauth2
from sqlalchemy.orm import Session
from typing import List
from ..repository import summaryMetricRepo
get_db = database.get_db
router = APIRouter(
    prefix="/summary_metrics",
    tags=['summaryMetrics']

)

@router.get('/', response_model=List[schemas.ShowSummaryMetric])
def all(db: Session = Depends(get_db)):
    return summaryMetricRepo.get_all(db)

@router.post('/', status_code=201)
def create(request: schemas.SummaryMetric, db: Session = Depends(get_db)):
    return summaryMetricRepo.create(request, db)

@router.delete('/{id}', status_code=204)
def destroy(id, db:Session = Depends(get_db)):
    return summaryMetricRepo.destroy(id, db)

@router.put('/{id}', status_code=202)
def update(id, request: schemas.SummaryMetric, db: Session = Depends(get_db)):
    return summaryMetricRepo.update(id, request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowSummaryMetric)
def show(id, db: Session = Depends(get_db)):
    return summaryMetricRepo.show(id, db)

