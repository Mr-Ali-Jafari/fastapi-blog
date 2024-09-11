from pydantic import BaseModel, EmailStr
from typing import List, Optional

class PermissionBase(BaseModel):
    name: str

class PermissionCreate(PermissionBase):
    pass

class Permission(PermissionBase):
    id: int

    class Config:
        orm_mode = True

class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    permission_ids: List[int] = []

class Role(RoleBase):
    id: int
    permissions: List[Permission] = []

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    role_ids: List[int] = []

class User(UserBase):
    id: int
    roles: List[Role] = []

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str



class BlogCreate(BaseModel):
    title: str
    content: str

class BlogUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class BlogResponse(BaseModel):
    id: int
    title: str
    content: str
    author_id: int

    class Config:
        orm_mode = True