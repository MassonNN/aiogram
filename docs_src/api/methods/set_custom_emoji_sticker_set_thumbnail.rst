#################################
setCustomEmojiStickerSetThumbnail
#################################

Returns: :obj:`bool`

.. automodule:: masogram.methods.set_custom_emoji_sticker_set_thumbnail
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: bool = await bot.set_custom_emoji_sticker_set_thumbnail(...)


Method as object
----------------

Imports:

- :code:`from masogram.methods.set_custom_emoji_sticker_set_thumbnail import SetCustomEmojiStickerSetThumbnail`
- alias: :code:`from masogram.methods import SetCustomEmojiStickerSetThumbnail`

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: bool = await bot(SetCustomEmojiStickerSetThumbnail(...))

As reply into Webhook in handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    return SetCustomEmojiStickerSetThumbnail(...)
