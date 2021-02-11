import datetime
import uuid
from typing import Optional

from .models import BookRequest
from .persistors import book_requests
from .persistors import books


def list_books():
    return books.items()


def create_request(book: str, email: str) -> Optional[BookRequest]:
    if book not in books.values():
        return None
    book_request = BookRequest(
        title=book, email=email, uid=uuid.uuid4(), timestamp=datetime.datetime.now()
    )
    book_requests[book_request.uid] = book_request
    return book_request


def get_request(uid: uuid.UUID) -> Optional[BookRequest]:
    return book_requests.get(uid, None)


def delete_request(uid: uuid.UUID) -> Optional[BookRequest]:
    return book_requests.pop(uid, None)
