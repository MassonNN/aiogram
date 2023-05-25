from masogram.types import Message, PhotoSize


def extract_photo(message: Message) -> PhotoSize:
    """ Extract photo from message """
    return message.photo[-1]
