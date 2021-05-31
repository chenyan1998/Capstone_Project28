from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
    position = Column(String)
    risk = Column(Integer)

class SummaryMetric(Base):
    __tablename__ = 'summaryMetrics'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)