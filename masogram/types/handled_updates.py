from __future__ import annotations

from typing import TYPE_CHECKING

from masogram.types.base import MutableTelegramObject
from ..dispatcher.event.handler import HandlerObject

if TYPE_CHECKING:
    from .update import Update


class _HandledUpdate(MutableTelegramObject):
    class Config:
        arbitrary_types_allowed = True


class HandledUpdate(_HandledUpdate):
    """
    Internal event, should be used to receive information about handled updates
    """

    update: Update
    """Handled update"""
    duraton: int
    """Duration of update handling in ms"""
    handler: HandlerObject
    """Handler which handled this update"""
