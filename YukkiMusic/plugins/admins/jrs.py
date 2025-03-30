from pyrogram import Client, filters
from pyrogram.types import Message
from YukkiMusic import app
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


@app.on_message(
    command(["السورس", "سورس", "المبرمج"])
)
async def mak(client: Client, message: Message):
    await message.reply_photo(
        photo="https://graph.org/file/2c3533c3282f7b809184c.jpg",
        caption="~ Team freedom \n~ king Source",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⦗ king ⦘", url="https://t.me/tpp_0"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "⦗ My works ⦘", url="https://t.me/QO_3O"
                    ),
                    InlineKeyboardButton(
                        "⦗ Kindness ⦘", url="https://t.me/En_d12"
                    ),
                ],
            ]
        ),
    )
