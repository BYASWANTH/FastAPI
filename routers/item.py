from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException, Query, APIRouter
import models, database, schemas, models
from sqlalchemy.orm import Session
from sqlalchemy import insert

router = APIRouter(tags = ['Item'])

@router.get("/item")
def get_item(db: Session = Depends(database.get_db)):
    items = db.query(models.item).all()
    return items

@router.post('/item', status_code = status.HTTP_201_CREATED)
def create_item(request : schemas.Item, db : Session = Depends(database.get_db)):
    # new_item = models.item(item = request.item, item_desc = request.item_desc, uom = request.uom, division = request.division, division_name = request.division_name, dept = request.dept, dept_name = request.dept_name, family = request.family, family_name = request.family_name, cclass = request.cclass, class_name = request.class_name, subclass = request.subclass, brand = request.brand, manufacturer = request.manufacturer, private_label = request.private_label, shelf_life = request.shelf_life, net_weight = request.net_weight, width = request.width, depth = request.depth, height = request.height, rtv_nrtv = request.rtv_nrtv, hsn = request.hsn, tax_cat = request.tax_cat, gst = request.gst, cess = request.cess, vat = request.vat, ad_valorem = request.ad_valorem, rpc = request.rpc, margin_type = request.margin_type, colour = request.colour, item_size = request.item_size, catch_wt = request.catch_wt, plu_code =request.plu_code, variant = request.variant, pack_type = request.pack_type, pack_size = request.pack_size, wattage = request.wattage, rating = request.rating, veg_nonveg = request.veg_nonveg, style = request.style, season = request.season, app = request.app, hz_ind = request.hz_ind, count_orig = request.count_orig, asin = request.asin, create_id = request.create_id, create_time = request.create_time, modify_id = request.modify_id, modify_time = request.modify_time)
    # new_item = models.item(**request.dict())
    # db.add(new_item)
    # db.commit()
    # db.refresh(new_item)
    # return new_item
    data = request.dict()
    flag = False
    if len(data["item"])<=100:
        pass
    else:
        flag = True
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail = f"the item  length is greater than 100")

    if not flag:
        new_data  = insert(models.item).values(data)
        db.execute(new_data)
        db.commit()    
        return request

@router.get('/item/{id}', response_model = schemas.showItem)
def get_particular_item(id, db: Session = Depends(database.get_db)):
    item = db.query(models.item).filter(models.item.item == id).first()
    if not item:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"the item {id} is not in the database")
    return item

@router.delete('/item/{id}', status_code = status.HTTP_204_NO_CONTENT)
def item_deleting(id, db: Session = Depends(database.get_db)):
    item = db.query(models.item).filter(models.item.item == id)
    if not item:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"the item {id} is not in the database")
    item.delete()
    db.commit()
    return f"the item {id} id deleted"

@router.put('/item/{id}', status_code = status.HTTP_202_ACCEPTED)
def item_updating(id, db: Session = Depends(database.get_db)):
    item = db.query(models.item).filter(models.item.item == id)
    if not item.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"the item {id} is not in the database")
    item.update({'uom':'updated uom1'})
    db.commit()
    return "updated successfully"
 