import uuid
from typing import List
from typing import Optional

from fastapi import APIRouter
from fastapi import HTTPException
from starlette.responses import Response

from . import models
from . import services

router = APIRouter()


@router.get("/")
async def root():
    """Return the Homepage."""
    return {"message": "API Documentation at /docs"}


@router.get("/books/", response_model=List[models.Book])
async def get_books() -> List[models.Book]:
    """Get all available books."""
    return services.list_books()


@router.post(
    "/request/",
    response_model=models.BookRequest,
    status_code=201,
    responses={404: {"model": models.Message}},
)
async def create_book_request(
    item: models.BookCreateRequest,
) -> Optional[models.BookRequest]:
    """Create a new book request."""
    book_request = services.create_request(item.title, item.email)
    if not book_request:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_request


@router.get("/request/", response_model=List[models.BookRequest])
async def get_all_requests():
    """Return all the requests in the db."""
    return services.list_requests()


@router.get(
    "/request/{item_id}",
    response_model=models.BookRequest,
    responses={404: {"model": models.Message}},
)
async def get_book_request(item_id: uuid.UUID):
    """Get a book request."""
    book_request = services.get_request(item_id)
    if not book_request:
        raise HTTPException(status_code=404, detail="Request not found")
    return book_request


@router.delete(
    "/request/{item_id}",
    status_code=204,
    response_class=Response,
    responses={404: {"model": models.Message}},
)
async def delete_book_request(item_id: uuid.UUID) -> None:
    """Delete a book request."""
    book_request = services.delete_request(item_id)
    if not book_request:
        raise HTTPException(status_code=404, detail="Request not found")
