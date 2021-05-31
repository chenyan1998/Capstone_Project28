from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException
def get_all(db: Session):
    summaryMetrics = db.query(models.SummaryMetric).all()
    return summaryMetrics

def create(request: schemas.SummaryMetric, db: Session):
    new_summary_metric = models.SummaryMetric(title=request.title, content=request.content)
    db.add(new_summary_metric)
    db.commit()
    db.refresh(new_summary_metric)
    return new_summary_metric

def destroy(id:int, db: Session):
    summary_metric = db.query(models.SummaryMetric).filter(models.SummaryMetric.id==id)
    if not summary_metric.first():
        raise HTTPException(status_code=404, detail=f'SummaryMetric with id {id} not found')
    summary_metric.delete(synchronize_session=False)
    db.commit()
    return {'done'}

def update(id:int, request:schemas, db: Session):
    summary_metric = db.query(models.SummaryMetric).filter(models.SummaryMetric.id == id)
    if not summary_metric.first():
        raise HTTPException(status_code=404, detail=f'SummaryMetric with id {id} not found')
    summary_metric.update(request)
    db.commit()
    return 'update'

def show(id:int, db: Session):
    summary_metric = db.query(models.SummaryMetric).filter(models.SummaryMetric.id == id).first()
    if not summary_metric:
        raise HTTPException(status_code=404, detail = f'SummaryMetric with the {id} is not available')
    return summary_metric
