"""Test the service functions."""
import uuid
from datetime import datetime

from app import persistors
from app import services


def test_list_books():
    """Return all books."""
    assert services.list_books()[0].pk == 1
    assert services.list_books()[0].title == "The Colour of Magic"


def test_list_books_len():
    """Assert that we have the right ammount of books."""
    assert len(services.list_books()) == 41


def test_create_request_no_book_for_title():
    """Return None if a book request cannot be created."""
    assert services.create_request("no such tile", "lala") is None


def test_create_request():
    """Test that a book request is created when book exists and valid email."""
    request = services.create_request("Mort", "me@example.test")

    assert request.email == "me@example.test"
    assert request.title == "Mort"
    assert persistors.book_requests[request.uid] == request


def test_get_request():
    """Get a book."""
    a_request = persistors.BookRequestDict(
        uid=uuid.uuid4(),
        title="XXX",
        email="me@example.test",
        timestamp=datetime(2000, 12, 31),
    )
    persistors.book_requests[a_request["uid"]] = a_request

    request = services.get_request(a_request["uid"])

    assert request.email == "me@example.test"
    assert request.title == "XXX"
    assert request.timestamp == datetime(2000, 12, 31)
    assert request.uid == a_request["uid"]


def test_get_request_not_found():
    """Return none when the request is not found."""
    assert services.get_request(uuid.uuid4()) is None


def test_delete_request():
    """Delete a request."""
    a_request: persistors.BookRequestDict = {
        "uid": uuid.uuid4(),
        "title": "XXX",
        "email": "me@example.test",
        "timestamp": datetime(2000, 12, 31),
    }
    persistors.book_requests[a_request["uid"]] = a_request

    request = services.delete_request(a_request["uid"])

    assert request.email == "me@example.test"
    assert request.title == "XXX"
    assert request.timestamp == datetime(2000, 12, 31)
    assert request.uid == a_request["uid"]
    assert request.uid not in persistors.book_requests.keys()


def test_list_requests():
    """List all requests."""
    persistors.book_requests = {}
    a_request: persistors.BookRequestDict = {
        "uid": uuid.uuid4(),
        "title": "XXX",
        "email": "me@example.test",
        "timestamp": datetime(2000, 12, 31),
    }
    persistors.book_requests[a_request["uid"]] = a_request
    b_request: persistors.BookRequestDict = {
        "uid": uuid.uuid4(),
        "title": "XXX",
        "email": "me@example.test",
        "timestamp": datetime(2000, 12, 31),
    }
    persistors.book_requests[b_request["uid"]] = b_request

    requests = list(services.list_requests())

    assert len(requests) == 2
    assert requests[0] == a_request
