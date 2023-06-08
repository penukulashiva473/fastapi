from fastapi import FastAPI
from . import  models
from .database import engine
from  .routers import blog, user

app = FastAPI()

models.Base.metadata.create_all(engine)

# app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)




# from typing import List
# from typing import Union
# from fastapi import FastAPI,Depends,status,Response, HTTPException
# from . import schemas,hashing,models
# from .database import engine, SessionLocal
# from sqlalchemy.orm import Session
# from .hashing import Hash



# app = FastAPI()

# models.Base.metadata.create_all(engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.post("/blog",status_code=status.HTTP_201_CREATED)
# async def create_item(request: schemas.BlogBase, db: Session=Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.delete("/blog/{id}",status_code=status.HTTP_204_NO_CONTENT)
# async def destroy(id, db: Session=Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id )
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available" )

#     blog.delete(synchronize_session=False)
#     db.commit()
#     return 'done'


# @app.put("/blog/{id}",status_code=status.HTTP_202_ACCEPTED)
# async def update(id,request: schemas.BlogBase, db: Session=Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id )
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available" )

#     blog.update({'title':request.title, 'body':request.body})
#     db.commit()
#     return 'Updated'


# @app.get("/blog",response_model=List[schemas.Blog])
# async def all(db: Session=Depends(get_db)):
#     all_blogs = db.query(models.Blog).all()
#     return all_blogs


# @app.get("/blog/{id}",status_code=200, response_model=schemas.ShowBlog)
# async def show(id,response:Response,db: Session=Depends(get_db)):
#     blog_with_id = db.query(models.Blog).filter(models.Blog.id == id ).first()
#     if not blog_with_id:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available" )
        
#     return blog_with_id






# @app.post('/user',response_model=schemas.ShowUser)
# def create_user(request: schemas.User,db: Session = Depends(get_db)):
#     new_user = models.User(name=request.name, email=request.email,password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get('/user/{id}',response_model=schemas.ShowUser)
# def get_user(id:int,db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id ).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not available" )
        
#     return user