from typing import List
from fastapi import APIRouter,Depends,Response,status,HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog])
async def all(db: Session=Depends(database.get_db)):
    return blog.get_all(db)




@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_item(request: schemas.BlogBase, db: Session=Depends(get_db)):
     return blog.create(request, db)






@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id,request, db)



@router.get("/{id}",status_code=200, response_model=schemas.ShowBlog)
async def show(id,response:Response,db: Session=Depends(get_db)):
    return blog.show(id,db)



@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id, db: Session=Depends(get_db)):
     return blog.destroy(id,db)