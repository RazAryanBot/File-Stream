# (c) @biisal @adarsh

from biisal.bot import StreamBot
from biisal.vars import Var
import logging
logger = logging.getLogger(__name__)
from biisal.bot.plugins.stream import MY_PASS
from biisal.utils.human_readable import humanbytes
from biisal.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from biisal.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup
from biisal.vars import bot_name , bisal_channel , bisal_grp


SRT_TXT = """<b>Hᴇʏ {}!,

I ᴀᴍ ᴀ Fɪʟᴇ ᴛᴏ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ ᴡɪᴛʜ Cʜᴀɴɴᴇʟ sᴜᴘᴘᴏʀᴛ.

Sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ ᴀɴᴅ ɢᴇᴛ ᴀ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴᴅ sᴛʀᴇᴀᴍᴀʙʟᴇ ʟɪɴᴋ.

Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : <a href='https://t.me/LazyHUB'>🧑🏻‍💻𐏓꯭꯭Ⱡᴀ̄͞ᴢ̄͞ʏ̄͞ 🄷🅄🄱</a></b>"""

@StreamBot.on_message(filters.command("start") & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.NEW_USER_LOG,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__ꜱᴏʀʀʏ, ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ꜰᴏʀ ᴜꜱɪɴɢ ᴍᴇ. ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ__\n\n  **𝙃𝙚 𝙬𝙞𝙡𝙡 𝙝𝙚𝙡𝙥 𝙮𝙤𝙪**",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://telegra.ph/file/5eb253f28ed7ed68cb4e6.png",
                caption=""""<b>Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ 😊\n\nDᴜᴇ ᴛᴏ sᴇʀᴠᴇʀ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ !</b>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ Nᴏᴡ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<b>sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ. ᴘʟᴇᴀsᴇ <a href='https://t.me/LazyPrince_Bot'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ sᴜᴘᴘᴏʀᴛ.</a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
    chat_id=m.chat.id,
    photo="https://telegra.ph/file/d813fe75a3ac675ef34b7.jpg",
    caption= SRT_TXT.format(m.from_user.mention(style="md")),
    reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("⚠️ Dɪsᴄʟᴀɪᴍᴇʀ ⚠️", url=f"https://www.google.com")],
            [
                 InlineKeyboardButton("Uᴘᴅᴀᴛᴇꜱ 🔔", url=bisal_channel),
                 InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ 🆘", url=bisal_grp)
            ],
            [InlineKeyboardButton("🧑🏻‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ 🧑🏻‍💻", callback_data="aboutDev")],

            [
                 InlineKeyboardButton("Aʙᴏᴜᴛ ♻️", callback_data="about"),
                 InlineKeyboardButton("Hᴇʟᴘ ℹ️", callback_data="help")
            ]
        ]
    )
)

@StreamBot.on_message(filters.command("help") & filters.private )
async def help_cd(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.NEW_USER_LOG,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__ꜱᴏʀʀʏ, ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ꜰᴏʀ ᴜꜱɪɴɢ ᴍᴇ. ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ__\n\n  **𝙃𝙚 𝙬𝙞𝙡𝙡 𝙝𝙚𝙡𝙥 𝙮𝙤𝙪**",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://telegra.ph/file/5eb253f28ed7ed68cb4e6.png",
                caption=""""<b>Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ 😊\n\nDᴜᴇ ᴛᴏ sᴇʀᴠᴇʀ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ !</b>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🔐", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<b>sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ.ᴘʟᴇᴀsᴇ <a href='https://t.me/LazyPrince_Bot'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ sᴜᴘᴘᴏʀᴛ</a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
    chat_id=m.chat.id,
    photo="https://telegra.ph/file/d813fe75a3ac675ef34b7.jpg",
    caption=f"<b>ᴡᴇ ᴅᴏɴᴛ ɴᴇᴇᴅ ᴍᴀɴʏ <a href='https://t.me/LazyHUB'>ᴄᴏᴍᴍᴀɴᴅs</a> ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ 🤩.\n\nᴊᴜsᴛ sᴇɴᴅ ᴍᴇ <a href='https://t.me/LazyHUB'>ᴠɪᴅᴇᴏ ғɪʟᴇs</a> ᴀɴᴅ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ <a href='https://t.me/LazyHUB'>ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ & sᴛʀᴇᴀᴍᴀʙʟᴇ</a> ʟɪɴᴋ.\n\nᴏʀ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ɪɴ <a href='https://t.me/LazyHUB'>ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ</a>. ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴀɴᴅ sᴇᴇ ᴍʏ ᴍᴀɢɪᴄ 😎</b>",
    reply_markup=InlineKeyboardMarkup(
        [
            [   
                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=bisal_channel)
            ],
            [
                InlineKeyboardButton("ᴅɪsᴄʟᴀɪᴍᴇʀ", url=f"https://www.google.com")
            ],
            [
                InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url=bisal_grp),

            ],
            [
                InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),

            ]

        ]
    )
)



@StreamBot.on_callback_query()
async def cb_handler(client, query):
    data = query.data
    if data == "close_data":
        await query.message.delete()


    if data == "start":
        await query.message.edit_caption(
        caption= SRT_TXT.format(query.from_user.mention(style="md")),
        reply_markup=InlineKeyboardMarkup(
                [
            [InlineKeyboardButton("⚠️ Dɪsᴄʟᴀɪᴍᴇʀ ⚠️", url=f"https://www.google.com")],
            [
                 InlineKeyboardButton("Uᴘᴅᴀᴛᴇꜱ 🔔", url=bisal_channel),
                 InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ 🆘", url=bisal_grp)
            ],
            [InlineKeyboardButton("🧑🏻‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ 🧑🏻‍💻", callback_data="aboutDev")],

            [
                 InlineKeyboardButton("Aʙᴏᴜᴛ ♻️", callback_data="about"),
                 InlineKeyboardButton("Hᴇʟᴘ ℹ️", callback_data="help")
            ]
        ]
            )
        )

    
    elif data == "about":
        await query.message.edit_caption(
            caption=f"<b>Mʏ Nᴀᴍᴇ :<a href='https://t.me/FileTo_LinksBot'>{bot_name}</a>\nAᴅᴍɪɴ : <a href='https://t.me/LazyPrince_Bot'>𐏓꯭꯭Ⱡᴀ̄͞ᴢ̄͞ʏ̄͞ P̸̲͟ʀ̲̄͟͞ɪ̲̄͟͞ɴ̲̄͟͞ᴄ̲̄͟͞ᴇ̲̄͟͞𐏓⚔</a>\nHᴏsᴛᴇᴅ ᴏɴ : Pʀɪᴠᴀᴛᴇ Sᴇʀᴠᴇʀ\nDᴀᴛᴀʙᴀsᴇ : Mᴏɴɢᴏ DB\nLᴀɴɢᴜᴀɢᴇ : Pʏᴛʜᴏɴ 3</b>",
            reply_markup=InlineKeyboardMarkup(
                [[ 
                     InlineKeyboardButton("🏠 Hᴏᴍᴇ", callback_data="start"),
                     InlineKeyboardButton("🔐 Cʟᴏsᴇ", callback_data="close_data")
                  ]]
            )
        )
    elif data == "help":
        await query.message.edit_caption(
        caption=f"<b>ᴡᴇ ᴅᴏɴᴛ ɴᴇᴇᴅ ᴍᴀɴʏ <a href='https://t.me/LazyHUB'>ᴄᴏᴍᴍᴀɴᴅs</a> ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ 🤩.\n\nᴊᴜsᴛ sᴇɴᴅ ᴍᴇ <a href='https://t.me/LazyHUB'>ᴠɪᴅᴇᴏ ғɪʟᴇs</a> ᴀɴᴅ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ <a href='https://t.me/LazyHUB'>ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ & sᴛʀᴇᴀᴍᴀʙʟᴇ</a> ʟɪɴᴋ.\n\nᴏʀ ʏᴏᴜ ᴄᴀɴ ᴀʟꜱᴏ ᴜsᴇ ᴍᴇ ɪɴ <a href='https://t.me/LazyHUB'>ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ</a> ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴀɴᴅ sᴇᴇ ᴍʏ ᴍᴀɢɪᴄ. 😎</b>",
            reply_markup=InlineKeyboardMarkup(
[[ 
                     InlineKeyboardButton("🏠 Hᴏᴍᴇ", callback_data="start"),
                     InlineKeyboardButton("🔐 Cʟᴏsᴇ", callback_data="close_data")
                  ]]            )
        )
    elif data == "aboutDev":
        # please don't steal credit
        await query.message.edit_caption(
            caption=f"<b>Hᴇʏ ᴅᴇᴀʀ... ɪᴍ <a href='https://t.me/LazyPrince_Bot'>𐏓꯭꯭Ⱡᴀ̄͞ᴢ̄͞ʏ̄͞ P̸̲͟ʀ̲̄͟͞ɪ̲̄͟͞ɴ̲̄͟͞ᴄ̲̄͟͞ᴇ̲̄͟͞𐏓⚔</a>\n\nɪ ᴀᴍ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏғ ᴛʜɪs ʙᴏᴛ..ᴀɴᴅ ɪ ᴍᴀᴅᴇ ᴛʜᴇ ʙᴏᴛ ʙʏ ʜᴇʟᴘ ᴏғ <a href='https://github.com/'>ᴀᴅᴀʀsʜ</a>\n\nʙᴏᴛ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://t.me/LazyPrince_Bot'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>",
            reply_markup=InlineKeyboardMarkup(
                [[ 
                     InlineKeyboardButton("🏠 Hᴏᴍᴇ", callback_data="start"),
                     InlineKeyboardButton("🔐 Cʟᴏsᴇ", callback_data="close_data")
                  ]]            )
        )
