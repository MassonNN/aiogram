from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from .base import TelegramMethod


class DeleteWebhook(TelegramMethod[bool]):
    """
    Use this method to remove webhook integration if you decide to switch back to :class:`masogram.methods.get_updates.GetUpdates`. Returns :code:`True` on success.

    Source: https://core.telegram.org/bots/api#deletewebhook
    """

    __returning__ = bool
    __api_method__ = "deleteWebhook"

    drop_pending_updates: Optional[bool] = None
    """Pass :code:`True` to drop all pending updates"""
