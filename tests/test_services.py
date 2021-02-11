"""Test the service functions."""
import uuid
from datetime import datetime

from app import persistors
from app import services


def test_list_books():
    assert services.list_books()[0].pk == 1
    assert services.list_books()[0].title == "The Colour of Magic"


def test_list_books_len():
    assert len(services.list_books()) == 41


def test_create_request_no_book_for_title():
    assert services.create_request("no such tile", "lala") is None


def test_create_request():
    request = services.create_request("Mort", "me@example.test")
    assert request.email == "me@example.test"
    assert request.title == "Mort"
    assert persistors.book_requests[request.uid] == request


def test_get_request():
    a_request = persistors.BookRequest(
        uid=uuid.uuid4(),
        title="XXX",
        email="me@example.test",
        timestamp=datetime(2000, 12, 31),
    )
    persistors.book_requests[a_request.uid] = a_request

    request = services.get_request(a_request.uid)

    assert request.email == "me@example.test"
    assert request.title == "XXX"
    assert request.timestamp == datetime(2000, 12, 31)
    assert request.uid == a_request.uid


def test_get_request_not_found():
    assert services.get_request(uuid.uuid4()) is None


def test_delete_request():
    a_request = persistors.BookRequest(
        uid=uuid.uuid4(),
        title="XXX",
        email="me@example.test",
        timestamp=datetime(2000, 12, 31),
    )
    persistors.book_requests[a_request.uid] = a_request

    request = services.delete_request(a_request.uid)

    assert request.email == "me@example.test"
    assert request.title == "XXX"
    assert request.timestamp == datetime(2000, 12, 31)
    assert request.uid == a_request.uid
    assert request.uid not in persistors.book_requests.keys()


def test_list_requests():
    persistors.book_requests = {}
    a_request = persistors.BookRequest(
        uid=uuid.uuid4(),
        title="XXX",
        email="me@example.test",
        timestamp=datetime(2000, 12, 31),
    )
    persistors.book_requests[a_request.uid] = a_request
    b_request = persistors.BookRequest(
        uid=uuid.uuid4(),
        title="XXX",
        email="me@example.test",
        timestamp=datetime(2000, 12, 31),
    )
    persistors.book_requests[b_request.uid] = b_request

    requests = services.list_requests()

    assert len(requests) == 2

    assert requests[0] == a_request
