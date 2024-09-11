from sqlalchemy.orm import Session
from app.models.models import Blog
from app.schemas.schemas import BlogCreate, BlogUpdate



def create_blog(db: Session, blog_create: BlogCreate, author_id: int):
    new_blog = Blog(**blog_create.dict(), author_id=author_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def update_blog(db: Session, blog_id: int, blog_update: BlogUpdate):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        return None
    for key, value in blog_update.dict(exclude_unset=True).items():
        setattr(blog, key, value)
    db.commit()
    db.refresh(blog)
    return blog

def delete_blog(db: Session, blog_id: int):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if blog:
        db.delete(blog)
        db.commit()
    return blog


def get_blog(db: Session, blog_id: int):
    return db.query(Blog).filter(Blog.id == blog_id).first()

def get_blogs(db: Session):
    return db.query(Blog).all()