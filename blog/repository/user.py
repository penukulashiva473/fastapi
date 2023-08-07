
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status
from ..hashing import Hash

def create(request: schemas.User,db:Session):
    new_user = models.User(username=request.username,email=request.email,password=Hash.bcrypt(request.password),full_name=request.full_name,age=request.age,gender=request.gender)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

