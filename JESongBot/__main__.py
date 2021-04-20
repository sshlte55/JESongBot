# Infinity BOTs <https://t.me/GB_031099>
# @GB_031099

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from ɢʙ sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ɢʙ sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ import Jebot as app
from ɢʙ sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ import LOGGER

pm_start_text = """
Heya [{}](tg://user?id={}), I'm ɢʙ sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ🎵

Do /help for know my commands

A bot by @GB_031099
"""

help_text = """
My commands👇

- /song <song name>: download songs via Youtube
- /saavn <song name>: download songs via JioSaavn
- /deezer <song name>: download songs via Deezer
- Send youtube url to my pm for download it on audio format

A bot by @GB_031099

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Source", url="https://github.com/sshlte55/JESongBot"
                    ),
                    InlineKeyboardButton(
                        text="Dev", url="https://t.me/GB_031099"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def start(client, message):
    await message.reply(help_text)

app.start()
LOGGER.info("JESongBot is online.")
idle()
