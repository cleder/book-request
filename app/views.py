import uuid
from typing import Any, Tuple
from typing import List
from typing import Optional

from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr

from . import models
from . import services


router = APIRouter()


@router.get("/")
async def root():
    """Return the Homepage."""
    return {"message": "API Documentation at /docs"}


@router.get("/books/")
async def get_books() -> List[Tuple[int, str]]:
    """Get all available books."""
    return services.list_books()


@router.post("/request/")
async def create_book_request(
    item: models.BookCreateRequest,
) -> Optional[models.BookRequest]:
    """Create a new book request."""
    book_request = services.create_request(item.title, item.email)
    if not book_request:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_request


@router.get("/request/{item_id}")
async def get_book_request(item_id: uuid.UUID):
    """Get a book request."""
    book_request = services.get_request(item_id)
    if not book_request:
        raise HTTPException(status_code=404, detail="Request not found")
    return book_request


@router.delete("/request/{item_id}")
async def delete_book_request(item_id: uuid.UUID) -> None:
    """Delete a book request."""
    book_request = services.delete_request(item_id)
    if not book_request:
        raise HTTPException(status_code=404, detail="Request not found")
