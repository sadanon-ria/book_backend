from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from database.db import get_session
from model.book import BookBase, BookPublic, BookCreate, BookUpdate, Book

router = APIRouter()

SessionDep = Annotated[Session, Depends(get_session)]

@router.get("/books", response_model=list[BookPublic])
def read_books(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=10)] = 10,
):
    books = session.exec(select(Book).offset(offset).limit(limit)).all()
    return books

@router.get("/book/{book_id}", response_model=BookPublic)
def read_book(book_id: int, session: SessionDep):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="book not found")
    return book

@router.post("/book/create", response_model=BookPublic)
def create_book(book: BookCreate, session: SessionDep):
    db_book = Book(**book.dict())
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book


@router.patch("/book/{book_id}", response_model=BookPublic)
def update_book(book_id: int, book: BookUpdate, session: SessionDep):
    book_db = session.get(Book, book_id)
    if not book_db:
        raise HTTPException(status_code=404, detail="book not found")
    book_data = book.model_dump(exclude_unset=True)
    book_db.sqlmodel_update(book_data)
    session.add(book_db)
    session.commit()
    session.refresh(book_db)
    return book_db


@router.delete("/book/{book_id}")
def delete_book(book_id: int, session: SessionDep):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="book not found")
    session.delete(book)
    session.commit()
    return {"ok": True}



# @router.post("/book/", response_model=Book)
# def create_book(book: Book, session: SessionDep):
#     session.add(book)
#     session.commit()
#     session.refresh(book)
#     return book


# @router.get("/books/", response_model=list[Book])
# def read_books(
#     session: SessionDep,
#     offset: int = 0,
#     limit: Annotated[int, Query(le=100)] = 100,
# ):
#     books = session.exec(select(Book).offset(offset).limit(limit)).all()
#     return books


# @router.get("/book/{book_id}", response_model=Book)
# def read_book(book_id: int, session: SessionDep):
#     book = session.get(Book, book_id)
#     if not book:
#         raise HTTPException(status_code=404, detail="book not found")
#     return book


# @router.delete("/book/{book_id}")
# def delete_book(book_id: int, session: SessionDep):
#     book = session.get(Book, book_id)
#     if not book:
#         raise HTTPException(status_code=404, detail="book not found")
#     session.delete(book)
#     session.commit()
#     return {"ok": True}
