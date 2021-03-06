# TG_MP3_Download_Bot

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TGMP3DownloadBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from TGMP3DownloadBot import MP3DownloadBot as app
from TGMP3DownloadBot import LOGGER

pm_start_text = """
 ๐ง Telegram Mahnฤฑ Yรผklษmษ Botu ๐ง
Salam [{}](tg://user?id={}) ๐ Mษn Telegram manhi  yรผklษyษn Botu ๐ง

โซ ฤฐstษdiyiniz Mahnฤฑnฤฑ MP3 ลษklindษ yรผklษyษ bilษrsizโจ: `/song Iman Zaman - Qฤฑzฤฑm Qฤฑzฤฑm`

โช ๐๐ฎฬ๐ฆ๐ฎ๐ง๐: `/song zawanbeatsz`

~ ๐ ๏ธ ๐บ๐๐๐๐๐๐ @SOQrup  
"""


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
                             text=" ๐ ๏ธ ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ ๐๐ก๐๐ญ ",
                             url="https://t.me/SOQrup"),
                         InlineKeyboardButton(
                             text=" ๐ ๐๐๐ง๐ข๐ฅ๐ข๐ค๐ฅ๐๐ซ ๐๐๐ง๐๐ฅฤฑ ",
                             url="https://t.me/ledyplaylist")
                    ],
                    [
                        InlineKeyboardButton(
                             text="๐จโ๐ป ๐๐๐ก๐ข๐ ",
                             url="https://t.me/Tenha055"),
                         InlineKeyboardButton(
                             text=" ๐๐ฎ๐ฌ๐ข๐ ๐๐ฅ๐๐ฒ๐๐ซ ",
                             url="https://t.me/musicplayerasistant_bot")
                    ],
                    [
                        InlineKeyboardButton(
                            text=" โ๏ธ ๐๐๐ฏ๐๐ฅ๐จ๐ฉ๐๐ซ ",
                             url="https://t.me/ruzgar_alican") 
                    
                    ]
            ]
        ),
    else:
   
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


app.start()
LOGGER.info("TG Mahnฤฑ Yรผklษmษ Botu onlayndฤฑr ๐จโ๐ป .")
idle()
