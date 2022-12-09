# Copyright (C) 2022 by Radenihbos@Github, < https://github.com/Radenihbos >.
# © by @Radenihboss
# t.me/Jomblosuport & t.me/Jombloproject


import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


logging.basicConfig(
    level=logging.INFO, format="%(name)s - [%(levelname)s] - %(message)s"
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID", "16039780"))
api_hash = os.environ.get("API_HASH", "43c5751eb09007121dcb3ee256213dc9")
bot_token = os.environ.get("TOKEN", "5622576319:AAHxkZnDVk2cJcYwpevVpiJZO307KcVG8uY")
client = TelegramClient("client", api_id, api_hash).start(bot_token=bot_token)
spam_chats = []


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ɪ ᴀᴍ ᴀʟɪᴠᴇ 🥺")
    await event.reply(
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n✪ ɪ ᴀᴍ ⋆˹㊭˼⋆ᴊᴏᴍʙʟᴏ ᴍᴇɴᴛɪᴏɴ⋆˹㊭˼⋆ ᴛʜᴇ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ\n✪ ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ʀᴜɴ /help..\n\n┏━━━━━━━━━━━━━━━━━┓\n┣★ ᴏᴡɴᴇʀ    : [ʙ̷ᴧɴɢ ꝛᴀ̷ᴅεɴ](https://t.me/Radenihboss)\n┣★ ᴜᴘᴅᴀᴛᴇs › : [ᴊᴏᴍʙʟᴏ ʜᴇʟᴘ](t.me/Jomblosuport)┓\n┣★ ʀᴇᴘᴏ › : [ᴊᴏᴍʙʟᴏ ʀᴇᴘᴏ](https://github.com/Radenihbos/Jomblotagall)\n┗━━━━━━━━━━━━━━━━━┛\n\n💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ\nᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](https://t.me/Radenihboss) ...\n\n━━━━━━━━━━━━━━━━━━━━━━━━",
        link_preview=False,
        buttons=(
            [
                Button.url(
                    "☀︎︎️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ☀︎︎",
                    "https://t.me/JomblotagBot?startgroup=true",
                ),
            ],
            [
                Button.url("☀︎︎ ɢʀᴏᴜᴘ ☀︎︎︎", "https://t.me/Jomblosuport"),
                Button.url("☀︎︎ ᴄʜᴀɴɴᴇʟ ☀︎︎", "https://t.me/Jombloday"),
            ],
            [
                Button.url("☀︎︎ ᴀɪʀᴅʀᴏᴘ ☀︎︎️️", "https://t.me/coffeecryptoairdrop"),
                Button.url("☀︎︎ ɴɪɢʜᴛ ᴀᴅᴅɪᴄᴛɪᴠᴇ sᴇx ☀︎︎", "https://t.me/Nasnihbos"),
            ],
        ),
    )


@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ᴅᴇᴀʀ sᴛᴀʀᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴғ 🥺")
    helptext = "✪ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ ᴊᴏᴍʙʟᴏ ᴍᴇɴᴛɪᴏɴ\n\n✪ ᴄᴏᴍᴍᴀɴᴅ: /jombloall\n✪ ᴄᴏᴍᴍᴀɴᴅ: /cancel ᴛᴏ ᴄᴀɴᴄᴇʟ ɢᴏɪɴɢ ᴏɴ ᴘʀᴏᴄᴇss.\n✪ ᴄᴏᴍᴍᴀɴᴅ /admin ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴀᴅᴍɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ\n✪ Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ᴛᴇxᴛ ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs.\n✪ `Example: /mentionall Good Morning!`\n✪ Yᴏᴜ ᴄᴀɴ ʏᴏᴜ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ. Bᴏᴛ ᴡɪʟʟ ᴛᴀɢ ᴜsᴇʀs ᴛᴏ ᴛʜᴀᴛ ʀᴇᴘʟɪᴇᴅ ᴍᴇsssᴀɢᴇ."
    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("☀︎︎ ᴀɪʀᴅʀᴏᴘ", "https://t.me/coffeecryptoairdrop"),
                Button.url("ʏᴏᴜᴛᴜʙᴇ ☀︎︎", "https://youtube.com/channel/UCLZMrrb0C4F63WdD82VQrGw"),
            ]
        ),
    )


@client.on(events.NewMessage(pattern="^/owner$"))
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ᴅᴇᴀʀ sᴛᴀʀᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴғ 🥺")
    helptext = "✪ ᴏᴡɴᴇʀ ᴍᴇɴᴜ ᴏғ ᴊᴏᴍʙʟᴏ ᴍᴇɴᴛɪᴏɴ\n\n✪ ᴍʏ ᴏᴡɴᴇʀ ɪs [ʙ̷ᴧɴɢ ꝛᴀ̷ᴅεɴ](https://t.me/Radenihboss)\n✪ ᴏғғɪᴄɪᴀʟ ᴍᴇᴍʙᴇʀ ᴏғ ᴀɪʀᴅʀᴏᴘ\n✪ ʏᴏᴜᴛᴜʙᴇ [ᴄʜᴀɴɴᴇʟ](https://youtube.com/channel/UCLZMrrb0C4F63WdD82VQrGw)\n✪ ғᴜᴛᴜʀᴇ ᴀɴᴇsᴛʜᴇᴛɪᴄ."
    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("☀︎︎ ᴀɪʀᴅʀᴏᴘ", "https://t.me/coffeecryptoairdrop"),
                Button.url("ʏᴏᴜᴛᴜʙᴇ ☀︎︎", "https://youtube.com/channel/UCLZMrrb0C4F63WdD82VQrGw"),
            ]
        ),
    )


@client.on(events.NewMessage(pattern="^/jombloall ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be use in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("__Only admins can mention all!__")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("__Give me one argument!__")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "__I can't mention members for older messages! (messages which are sent before I'm added to group)__"
            )
    else:
        return await event.respond(
            "__Reply to a message or give me some text to mention others!__"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{usrtxt}\n\n{msg}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/admins|/admin|@admin|@admins ?(.*)"))
async def _(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond("sᴏʀʀʏ ʏᴏᴜ ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ᴀᴅᴍɪɴ ᴏɴʟʏ ɪɴ ɢʀᴏᴜᴘ")

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("ᴏɴʟʏ ᴀᴅᴍɪɴ ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴs")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "__ɪ ᴄᴀɴ'ᴛ ᴍᴇɴᴛɪᴏɴ ᴍᴇᴍʙᴇʀs ꜰᴏʀ ᴏʟᴅᴇʀ ᴍᴇssᴀɢᴇs! (ᴍᴇssᴀɢᴇs ᴡʜɪᴄʜ ᴀʀᴇ sᴇɴᴛ ʙᴇꜰᴏʀᴇ ɪ'ᴍ ᴀᴅᴅᴇᴅ ᴛᴏ ɢʀᴏᴜᴘ)__"
            )
    else:
        return await event.respond(
            "__ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs!__"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    chat = await event.get_input_chat()
    async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f" \n [{x.first_name}](tg://user?id={x.id})"
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{usrtxt}\n\n{msg}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    if not event.chat_id in spam_chats:
        return await event.respond("__There is no proccess on going...__")
    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("__Stopped.__")


print(">> JOMBLO TAG ALL WORKING <<")
client.run_until_disconnected()


# Copyright (C) 2022 by Radenihbos@Github, < https://github.com/Radenihbos >.
# © by @Radenihboss
# t.me/Jomblosuport & t.me/Jombloproject
