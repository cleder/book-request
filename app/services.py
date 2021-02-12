"""Services to hold the business logic independent from the views."""
import datetime
import uuid
from typing import List
from typing import Optional

from .models import Book
from .models import BookRequest
from .persistors import add_request
from .persistors import delete_request_by_id
from .persistors import get_all_books
from .persistors import get_all_requests
from .persistors import get_book_by_title
from .persistors import get_request_by_id


def list_books() -> List[Book]:
    """Return a list of books in the db."""
    return get_all_books()


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
    return add_request(book_request)


def get_request(uid: uuid.UUID) -> Optional[BookRequest]:
    """Get a book request."""
    return get_request_by_id(uid)


def list_requests() -> List[BookRequest]:
    """Return all the requests in the db."""
    return list(get_all_requests())


def delete_request(uid: uuid.UUID) -> Optional[BookRequest]:
    """Delete a book request."""
    return delete_request_by_id(uid)
