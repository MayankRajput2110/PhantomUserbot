"""Quickly make a decision
Syntax: .decide"""
from telethon import events
import requests
from userbot.utils import phantom_cmd, sudo_cmd



@borg.on(phantom_cmd("decide"))
@borg.on(sudo_cmd(pattern="decide", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    r = requests.get("https://yesno.wtf/api").json()
    await borg.send_message(
        event.chat_id,
        r["answer"],
        reply_to=message_id,
        file=r["image"]
    )
    await event.delete()
