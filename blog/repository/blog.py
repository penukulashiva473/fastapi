from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status

def create(request: schemas.Blog,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.key == request.key).first()
    if blog:
        return 0
    new_blog = models.Blog(key=request.key, value=request.value)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return {
            "status": "success",
            "message": "Data deleted successfully."
            }

def update(id:int,request:schemas.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.update({'key':request.key, 'value':request.value})
    db.commit()
    return {
            "status": "success",
            "message": "Data updated successfully."
            }

def show(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    return {
            "status": "success",
            "data": blog
            }