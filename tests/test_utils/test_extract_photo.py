from datetime import datetime

from masogram.types import Message, Chat, PhotoSize
from masogram.utils.extract_photo import extract_photo


def test_extract():
    test_photo_size = PhotoSize(file_id="some", file_unique_id="some_some", width=1, height=1)
    message = Message(
        message_id=1,
        date=datetime.utcnow(),
        chat=Chat(id=1, type="private"),
        photo=[test_photo_size, ]
    )
    assert extract_photo(message) == test_photo_size
