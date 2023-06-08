from typing import Union
from fastapi import FastAPI,Depends,status,Response, HTTPException
from . import schemas
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session



app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/blog",status_code=status.HTTP_201_CREATED)
async def create_item(request: schemas.Blog, db: Session=Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete("/blog/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id, db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id )
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available" )

    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


@app.put("/blog/{id}",status_code=status.HTTP_202_ACCEPTED)
async def update(id,request: schemas.Blog, db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id )
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available" )

    blog.update({'title':request.title, 'body':request.body})
    db.commit()
    return 'Updated'


@app.get("/blog")
async def all(db: Session=Depends(get_db)):
    all_blogs = db.query(models.Blog).all()
    return all_blogs


@app.get("/blog/{id}",status_code=200)
async def show(id,response:Response,db: Session=Depends(get_db)):
    blog_with_id = db.query(models.Blog).filter(models.Blog.id == id ).first()
    if not blog_with_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available" )
        
    return blog_with_id