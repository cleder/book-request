"""Pydandic Models."""
import datetime
import uuid

from pydantic import BaseModel
from pydantic import EmailStr


class BookCreateRequest(BaseModel):
    """Type to create a BookRequest."""

    title: str
    email: EmailStr


class BookRequest(BookCreateRequest):
    """A Book request object."""

    timestamp: datetime.datetime
    uid: uuid.UUID


class Book(BaseModel):
    """Book, has an id and a title."""

    pk: int
    title: str


class Message(BaseModel):
    """Error Message."""

    detail: str
