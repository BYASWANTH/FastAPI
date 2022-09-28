from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship

class item(Base):
    __tablename__ = 'item1'

    item = Column(String, primary_key = True, index = True) 
    item_desc = Column(String)
    uom = Column(String)

    item_in_cpmrpdc1 = relationship("cpmrp_dc", back_populates = "item_in_item1")

    __table_args__ = {'schema' : 'freshers_dev'}

class cpmrp_dc(Base):
    __tablename__ = 'cpmrp_dc1'

    item = Column(String, ForeignKey('freshers_dev.item1.item'), primary_key = True, index = True)
    dc_city = Column(String)
    cost = Column(String)
    mrp = Column(String)

    item_in_item1 = relationship("item", back_populates  = "item_in_cpmrpdc1")

    __table_args__ = {'schema' : 'freshers_dev'}

    