from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException, Query, APIRouter
import models, database, schemas, models
from sqlalchemy.orm import Session
from sqlalchemy import insert

router = APIRouter(tags = ['cpmrp_dc'])

@router.post('/citem', status_code = status.HTTP_201_CREATED)
def create_citem(request : schemas.cpmrp_dc, db : Session = Depends(database.get_db)):
    # hashedgkm = gkm_cxt.hash(request.gkm)
    data = request.dict()
    flag = False    
    if len(data["item"])<=100:
        pass
    else:
        flag = True
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail = f"the item  length is greater than 100")

    if not flag:
        cnew_data  = insert(models.cpmrp_dc).values(data)
        db.execute(cnew_data)
        db.commit()    
        return request


@router.get("/citem")
def get_citem(db: Session = Depends(database.get_db)):
    citems = db.query(models.cpmrp_dc).all()
    return citems

@router.get('/citem/{cid}', response_model = schemas.showCpmrpdc)
def get_particular_citem(cid, response : Response, db: Session = Depends(database.get_db)):
    citem = db.query(models.cpmrp_dc).filter(models.cpmrp_dc.item == cid).first()
    if not citem:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"the item {cid} is not in the database")
    return citem 

@router.delete('/citem/{cid}', status_code = status.HTTP_204_NO_CONTENT)
def citem_deleting(cid, db: Session = Depends(database.get_db)):
    citem = db.query(models.cpmrp_dc).filter(models.cpmrp_dc.item == cid)
    if not citem:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"the item {cid} is not in the database")
    citem.delete()
    db.commit()
    return f"the item {cid} is deleted"

@router.put('/citem/{cid}', status_code = status.HTTP_202_ACCEPTED)
def citem_updating(cid, db: Session = Depends(database.get_db)):
    citem = db.query(models.cpmrp_dc).filter(models.cpmrp_dc.item == cid)
    if not citem.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"the item {cid} is not in the database")
    citem.update({'dc_city':'kadapa'})
    db.commit()
    return "updated successfully"