from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException, Query, APIRouter
import models, database, schemas, models
from sqlalchemy.orm import Session
from sqlalchemy import insert

router = APIRouter(tags = ['joins'])

@router.get('/innerjoin')
def innser_join(db: Session = Depends(database.get_db)):
    ij = "select * from freshers_dev.item1 INNER JOIN freshers_dev.cpmrp_dc1 on item1.item = cpmrp_dc1.item;"
    # ij = db.query(models.item).join(models.cpmrp_dc).all()
    res = db.execute(ij)
    for i in res:
        yield i

@router.get('/leftouterjoin')
def innser_join(db: Session = Depends(database.get_db)):
    loj = "select * from freshers_dev.item1 LEFT JOIN freshers_dev.cpmrp_dc1 on item1.item = cpmrp_dc1.item;"
    res = db.execute(loj)
    for i in res:
        yield i

@router.get('/rightouterjoin')
def innser_join(db: Session = Depends(database.get_db)):
    roj = "select * from freshers_dev.item1 RIGHT JOIN freshers_dev.cpmrp_dc1 on item1.item = cpmrp_dc1.item;"
    res = db.execute(roj)
    for i in res:
        yield i

@router.get('/fullouterjoin')
def innser_join(db: Session = Depends(database.get_db)):
    foj = "select * from freshers_dev.item1 FULL OUTER JOIN freshers_dev.cpmrp_dc1 on item1.item = cpmrp_dc1.item;"
    res = db.execute(foj)
    for i in res:
        yield i