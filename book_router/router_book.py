from fastapi import APIRouter
from schemas.book_schema.schema_book import Book, BookResponse
from typing import Any
router = APIRouter()


@router.get("/allbooks", response_model= list[BookResponse])
async def read_all_books() -> Any:
    return [
        {
            "id": 1,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
        },
        {
            "id": 2,
            "title": "1984",
            "author": "George Orwell",
        },
    ]


@router.get("/books/book_id")
async def read_book(book_id: int):
    return {"book_id": book_id,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald"}


@router.get("/books")
async def read_books(year: int = None):
    if year:
        return {"year": year,
                "books": ["Book 1", "Book 2"]
                }

    return {"books": ["All Books"]}


@router.post("/book")
async def create_book(book: Book):
    return book
