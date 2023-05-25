from contextlib import contextmanager
from typing import Any, Awaitable, Callable, Dict, Iterator, Optional, Tuple

from masogram.dispatcher.middlewares.base import BaseMiddleware
from masogram.types import Chat, TelegramObject, Update, User
from masogram.utils.extract_photo import extract_photo


class ExtractPhotoMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        if event.message and event.message.photo:
            data['photo'] = extract_photo(event.message)
            return await handler(event, data)
