from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, DateTime, func

# class Book(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     title: str
#     author: str
#     published_year: Optional[int] = None
#     genre: Optional[str] = None
#     created_at: Optional[datetime] = Field(default=None)
#     updated_at: Optional[datetime] = Field(default=None)

class BookBase(SQLModel):
    title: str
    author: str
    published_year: Optional[int] = None
    genre: Optional[str] = None

# class Book(BookBase, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
    
#     created_at: Optional[datetime] = Field(
#         sa_column=Column(DateTime(timezone=True), server_default=func.now())
#     )
    
#     updated_at: Optional[datetime] = Field(
#         sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
#     )

class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)

class BookPublic(BookBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# สำหรับรับ input (POST/PUT)
class BookCreate(BookBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    

class BookUpdate(SQLModel):
    title: Optional[str] = None
    author: Optional[str] = None
    published_year: Optional[int] = None
    genre: Optional[str] = None
    updated_at: Optional[datetime] = None