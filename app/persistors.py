"""Dummy persistors"""
from uuid import UUID
from typing import Dict, Iterable, Optional, Tuple

from .models import BookRequest

books: Dict[int, str] = {
    1: "The Colour of Magic",
    2: "The Light Fantastic",
    3: "Equal Rites",
    4: "Mort",
    5: "Sourcery",
    6: "Wyrd Sisters",
    7: "Pyramids",
    8: "Guards! Guards!",
    9: "Faust Eric",
    10: "Moving Pictures",
    11: "Reaper Man",
    12: "Witches Abroad",
    13: "Small Gods",
    14: "Lords and Ladies",
    15: "Men at Arms",
    16: "Soul Music",
    17: "Interesting times",
    18: "Maskerade",
    19: "Feet of Clay",
    20: "Hogfather",
    21: "Jingo",
    22: "The Last Continent",
    23: "Carpe Jugulum",
    24: "The Fifth Elephant",
    25: "The Truth",
    26: "Thief of Time",
    27: "The Last Hero",
    28: "The Amazing Maurice And His Educated Rodents",
    29: "Night Watch",
    30: "The Wee Free Men",
    31: "Monstrous Regiment",
    32: "A Hat Full of Sky",
    33: "Going Postal",
    34: "Thud!",
    35: "Wintersmith",
    36: "Making Money",
    37: "Unseen Academicals",
    38: "I Shall Wear Midnight",
    39: "Snuff",
    40: "Raising Steam",
    41: "The Shepherd's Crown",
}

def get_all_books() -> Iterable[Tuple[int, str]]:
    """Get all books."""
    return books.items()

def get_book_by_title(title: str) -> Optional[Tuple[int, str]]:
    """Return the book with the given title or None if not found."""
    for k, v in books.items():
        if v == title:
            return k, v
    return None


book_requests: Dict[UUID, BookRequest] = {}
