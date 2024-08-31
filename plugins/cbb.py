#(©)Codeflix-Bots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ OWNER : <a href='tg://user?id={OWNER_ID}'>@pheonixxx01</a>\n○ JOIN : <a href='https://t.me/heueksi'>BACKUP CHANNEL</a>\n○ MEMBERSHIP PLANS : <a href='https://t.me/Russionleaks/5'>PLANS</a>\n○ GET PRIME : <a href='https://t.me/howtogetprime/4'>PRIME</a>\n○ FOR CONTENT REMOVAL MESSAGE HERE @Darkasff_bot",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("❌ CLOSE", callback_data = "close"),
                    InlineKeyboardButton('⭐ MEMBERSHIP', url='https://t.me/Russionleaks/5')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass