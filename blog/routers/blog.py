from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/data",
    tags=['Data']
)

get_db = database.get_db




@router.post('/api', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Blog,db: Session = Depends(get_db)):
    data = blog.create(request, db)
    if data:
        return {
                "status": "success",
                "message": "Data stored successfully."
                }
    else:
        return {
            "status": "KEY_EXISTS",
            "message": "- The provided key already exists in the database. To update an existing key, use the update API."
             }


@router.delete('/{id}')
def destroy(id:int, db: Session = Depends(get_db)):
    
    return blog.destroy(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id,request, db)


@router.get('/{id}', status_code=200)
def show(id:int, db: Session = Depends(get_db)):
    return blog.show(id,db)