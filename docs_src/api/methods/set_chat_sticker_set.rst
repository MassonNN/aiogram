#################
setChatStickerSet
#################

Returns: :obj:`bool`

.. automodule:: masogram.methods.set_chat_sticker_set
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: bool = await bot.set_chat_sticker_set(...)


Method as object
----------------

Imports:

- :code:`from masogram.methods.set_chat_sticker_set import SetChatStickerSet`
- alias: :code:`from masogram.methods import SetChatStickerSet`

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: bool = await bot(SetChatStickerSet(...))

As reply into Webhook in handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    return SetChatStickerSet(...)


As shortcut from received object
--------------------------------

- :meth:`masogram.types.chat.Chat.set_sticker_set`
