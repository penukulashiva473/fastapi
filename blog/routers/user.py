from fastapi import APIRouter
from .. import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/api/register')
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    data = user.create(request,db)
    if data:
        return {
                "status": "success",
                "message": "User successfully registered!",
                "data": data
                }
    else:
        return {
                "status": "error",
                "code": "INVALID_REQUEST",
                "message": "Invalid request. Please provide all required fields: username, email, password, full_name."
                }


