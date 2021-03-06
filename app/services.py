"""Services to hold the business logic independent from the views."""
import datetime
import uuid
from typing import List
from typing import Optional
from typing import cast

from .models import Book
from .models import BookRequest
from .persistors import BookRequestDict
from .persistors import add_request
from .persistors import delete_request_by_id
from .persistors import get_all_books
from .persistors import get_all_requests
from .persistors import get_book_by_title
from .persistors import get_request_by_id


def list_books() -> List[Book]:
    """Return a list of books in the db."""
    return [Book(pk=k, title=v) for k, v in get_all_books()]


def create_request(book: str, email: str) -> Optional[BookRequest]:
    """Create a book request when the book is in the db."""
    if not get_book_by_title(book):
        return None
    book_request = BookRequest(
        title=book,
        email=email,
        uid=uuid.uuid4(),
        timestamp=datetime.datetime.now(),
    )
    return BookRequest(**add_request(cast(BookRequestDict, book_request.dict())))


def get_request(uid: uuid.UUID) -> Optional[BookRequest]:
    """Get a book request."""
    bookrequest = get_request_by_id(uid)
    if bookrequest:
        return BookRequest(**bookrequest)
    return None


def list_requests() -> List[BookRequest]:
    """Return all the requests in the db."""
    return [BookRequest(**bookrequest) for bookrequest in get_all_requests()]


def delete_request(uid: uuid.UUID) -> Optional[BookRequest]:
    """Delete a book request."""
    bookrequest = delete_request_by_id(uid)
    if bookrequest:
        return BookRequest(**bookrequest)
    return None
