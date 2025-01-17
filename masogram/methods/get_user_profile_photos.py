from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..types import UserProfilePhotos
from .base import TelegramMethod


class GetUserProfilePhotos(TelegramMethod[UserProfilePhotos]):
    """
    Use this method to get a list of profile pictures for a user. Returns a :class:`masogram.types.user_profile_photos.UserProfilePhotos` object.

    Source: https://core.telegram.org/bots/api#getuserprofilephotos
    """

    __returning__ = UserProfilePhotos
    __api_method__ = "getUserProfilePhotos"

    user_id: int
    """Unique identifier of the target user"""
    offset: Optional[int] = None
    """Sequential number of the first photo to be returned. By default, all photos are returned."""
    limit: Optional[int] = None
    """Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100."""
