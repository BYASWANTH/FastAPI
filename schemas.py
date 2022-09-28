from dataclasses import Field
from pydantic import BaseModel
from typing import Optional, List

class Item(BaseModel):
    item : str  
    item_desc : str
    uom : str

    class Config:
        orm_mode = True

class cpmrp_dc(BaseModel):
    item : str
    dc_city : str
    cost : str
    mrp : str

    class Config:
        orm_mode = True

class showItem(BaseModel):
    item : str  
    item_desc : str
    uom : str
    item_in_cpmrpdc1 : List[cpmrp_dc] = []

    class Config:
        orm_mode = True

class showCpmrpdc(BaseModel):
    item : str
    dc_city : str
    cost : str
    mrp : str
    item_in_item1 : Item
    class Config:
        orm_mode = True
