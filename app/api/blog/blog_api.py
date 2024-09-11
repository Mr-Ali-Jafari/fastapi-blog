from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from app.config.database.database import get_db
from app.schemas.schemas import (
    BlogCreate,
    BlogUpdate, 
    BlogResponse,
)
from app.models.models import User
from app.api.login.login import get_current_user
from app.services.blog.blog_service import create_blog, get_blog, get_blogs,delete_blog,update_blog
router = APIRouter(
    prefix="/blog",
    tags=['Blog']
)



@router.post("/blogs/", response_model=BlogResponse)
def create_blog_api(blog_create: BlogCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_blog(db, blog_create, author_id=current_user.id)

@router.put("/blogs/{blog_id}", response_model=BlogResponse)
def update_blog_api(blog_id: int, blog_update: BlogUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    updated_blog = update_blog(db, blog_id, blog_update)
    if updated_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return updated_blog

@router.delete("/blogs/{blog_id}")
def delete_blog_api(blog_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    deleted_blog = delete_blog(db, blog_id)
    if deleted_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"message": "Blog deleted successfully"}



@router.get("/blogs/", response_model=list[BlogResponse])
def list_blogs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    blogs = get_blogs(db)
    return blogs

@router.get("/blogs/{blog_id}", response_model=BlogResponse)
def view_blog(blog_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    blog = get_blog(db, blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog