from fastapi import Depends, FastAPI, Query, HTTPException, Request, Response
from typing import Optional, Union
from sqlalchemy.orm import Session
from .infra.db.database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# middleware
# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#   response = Response("Internal Server Error", status_code=500)
#   try:
#     request.state.db = SessionLocal()
#     response = await call_next(request)
#   finally:
#     request.state.db.close()
#   return response