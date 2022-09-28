from curses import flash
from fastapi import FastAPI, Depends, status, Response, HTTPException, Query
from typing import Optional, List
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
# from passlib.context import CryptContext
from routers import item, cpmrp_dc, joins
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(item.router)  
app.include_router(cpmrp_dc.router)
app.include_router(joins.router)

