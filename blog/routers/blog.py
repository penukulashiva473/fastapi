from typing import List
from fastapi import APIRouter,Depends,Response,status,HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
# from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog])
async def all(db: Session=Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs




@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_item(request: schemas.BlogBase, db: Session=Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog




@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
async def update(id,request: schemas.BlogBase, db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id )
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available" )

    blog.update({'title':request.title, 'body':request.body})
    db.commit()
    return 'Updated'





@router.get("/{id}",status_code=200, response_model=schemas.ShowBlog)
async def show(id,response:Response,db: Session=Depends(get_db)):
    blog_with_id = db.query(models.Blog).filter(models.Blog.id == id ).first()
    if not blog_with_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available" )
        
    return blog_with_id




@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id, db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id )
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available" )

    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'