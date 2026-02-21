# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com


import asyncio
import importlib
import os
import threading
from flask import Flask, jsonify
from pyrogram import idle
from pyrogram.types import BotCommand
from pytgcalls.exceptions import NoActiveGroupCall
import config

# ↓↓↓ RENDER KEEP ALIVE + FLASK + WEBHOOK ↓↓↓
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return jsonify({
        "status": "alive",
        "bot": "Ajnabi Music",
        "message": "Bot is running on Render!"
    })

@app_flask.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app_flask.route('/webhook', methods=['POST'])
def webhook():
    return jsonify({"status": "received"}), 200

def run_flask():
    port = int(os.environ.get("PORT", 8000))
    app_flask.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

# Flask server ko background thread mein chalao
threading.Thread(target=run_flask, daemon=True).start()
# ↑↑↑ RENDER KEEP ALIVE END ↑↑↑


from AjnabiMusic import LOGGER, app, userbot
from AjnabiMusic.core.call import Nand
from AjnabiMusic.misc import sudo
from AjnabiMusic.plugins import ALL_MODULES
from AjnabiMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

COMMANDS = [
    BotCommand("start", "❖ sᴛᴀʀᴛ ʙᴏᴛ • ᴛᴏ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ"),
    BotCommand("help", "❖ ʜᴇʟᴘ ᴍᴇɴᴜ • ɢᴇᴛ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ"),
    BotCommand("ping", "❖ ᴘɪɴɢ ʙᴏᴛ • ᴄʜᴇᴄᴋ ᴘɪɴɢ ᴀɴᴅ sʏsᴛᴇᴍ sᴛᴀᴛs"),
    BotCommand("play", "❖ ᴘʟᴀʏ ᴀᴜᴅɪᴏ ᴏɴ ᴠᴄ • ᴛᴏ ᴘʟᴀʏ ᴀɴʏ ᴀᴜᴅɪᴏ ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ"),
    BotCommand("vplay", "❖ ᴘʟᴀʏ ᴠɪᴅᴇᴏ ᴏɴ ᴠᴄ • ᴛᴏ sᴛʀᴇᴀᴍ ᴀɴʏ ᴠɪᴅᴇᴏ ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ"),
    BotCommand("playrtmps", "❖ ᴘʟᴀʏ ʟɪᴠᴇ ᴠɪᴅᴇᴏ • sᴛʀᴇᴀᴍ ʟɪᴠᴇ ᴠɪᴅᴇᴏ ᴄᴏɴᴛᴇɴᴛ"),
    BotCommand("playforce", "❖ ғᴏʀᴄᴇ ᴘʟᴀʏ ᴀᴜᴅɪᴏ • ғᴏʀᴄᴇ ᴘʟᴀʏ ᴀɴʏ ᴀᴜᴅɪᴏ ᴛʀᴀᴄᴋ"),
    BotCommand("vplayforce", "❖ ғᴏʀᴄᴇ ᴘʟᴀʏ ᴠɪᴅᴇᴏ • ғᴏʀᴄᴇ ᴘʟᴀʏ ᴀɴʏ ᴠɪᴅᴇᴏ ᴛʀᴀᴄᴋ"),
    BotCommand("pause", "❖ ᴘᴀᴜsᴇ sᴛʀᴇᴀᴍ • ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴛʀᴇᴀᴍ"),
    BotCommand("resume", "❖ ʀᴇsᴜᴍᴇ sᴛʀᴇᴀᴍ • ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴘᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ"),
    BotCommand("skip", "❖ sᴋɪᴘ ᴛʀᴀᴄᴋ • sᴋɪᴘ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴛʀᴀᴄᴋ"),
    BotCommand("end", "❖ ᴇɴᴅ sᴛʀᴇᴀᴍ • sᴛᴏᴘ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ"),
    BotCommand("stop", "❖ sᴛᴏᴘ sᴛʀᴇᴀᴍ • sᴛᴏᴘ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴛʀᴇᴀᴍ"),
    BotCommand("queue", "❖ sʜᴏᴡ ǫᴜᴇᴜᴇ • ᴅɪsᴘʟᴀʏ ᴛʀᴀᴄᴋ ǫᴜᴇᴜᴇ ʟɪsᴛ"),
    BotCommand("auth", "❖ ᴀᴅᴅ ᴀᴜᴛʜ ᴜsᴇʀ • ᴀᴅᴅ ᴜsᴇʀ ᴛᴏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ʟɪsᴛ"),
    BotCommand("unauth", "❖ ʀᴇᴍᴏᴠᴇ ᴀᴜᴛʜ • ʀᴇᴍᴏᴠᴇ ᴜsᴇʀ ғʀᴏᴍ ᴀᴜᴛʜ ʟɪsᴛ"),
    BotCommand("authusers", "❖ ᴀᴜᴛʜ ʟɪsᴛ • sʜᴏᴡ ᴀʟʟ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs"),
    BotCommand("cplay", "❖ ᴄʜᴀɴɴᴇʟ ᴀᴜᴅɪᴏ • ᴘʟᴀʏ ᴀᴜᴅɪᴏ ɪɴ ᴄʜᴀɴɴᴇʟ"),
    BotCommand("cvplay", "❖ ᴄʜᴀɴɴᴇʟ ᴠɪᴅᴇᴏ • ᴘʟᴀʏ ᴠɪᴅᴇᴏ ɪɴ ᴄʜᴀɴɴᴇʟ"),
    BotCommand("cplayforce", "❖ ᴄʜᴀɴɴᴇʟ ғᴏʀᴄᴇ ᴀᴜᴅɪᴏ • ғᴏʀᴄᴇ ᴘʟᴀʏ ɪɴ ᴄʜᴀɴɴᴇʟ"),
    BotCommand("cvplayforce", "❖ ᴄʜᴀɴɴᴇʟ ғᴏʀᴄᴇ ᴠɪᴅᴇᴏ • ғᴏʀᴄᴇ ᴠɪᴅᴇᴏ ɪɴ ᴄʜᴀɴɴᴇʟ"),
    BotCommand("channelplay", "❖ ᴄᴏɴɴᴇᴄᴛ ᴄʜᴀɴɴᴇʟ • ʟɪɴᴋ ɢʀᴏᴜᴘ ᴛᴏ ᴄʜᴀɴɴᴇʟ"),
    BotCommand("loop", "❖ ʟᴏᴏᴘ ᴍᴏᴅᴇ • ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ʟᴏᴏᴘ"),
    BotCommand("stats", "❖ ʙᴏᴛ sᴛᴀᴛs • sʜᴏᴡ ʙᴏᴛ sᴛᴀᴛɪsᴛɪᴄs"),
    BotCommand("shuffle", "❖ sʜᴜғғʟᴇ ǫᴜᴇᴜᴇ • ʀᴀɴᴅᴏᴍɪᴢᴇ ᴛʀᴀᴄᴋ ᴏʀᴅᴇʀ"),
    BotCommand("seek", "❖ sᴇᴇᴋ ғᴏʀᴡᴀʀᴅ • sᴋɪᴘ ᴛᴏ sᴘᴇᴄɪғɪᴄ ᴛɪᴍᴇ"),
    BotCommand("seekback", "❖ sᴇᴇᴋ ʙᴀᴄᴋᴡᴀʀᴅ • ɢᴏ ʙᴀᴄᴋ ᴛᴏ ᴘʀᴇᴠɪᴏᴜs ᴛɪᴍᴇ"),
    BotCommand("song", "❖ ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ • ɢᴇᴛ ᴍᴘ3 ᴏʀ ᴍᴘ4 ғɪʟᴇ"),
    BotCommand("speed", "❖ ᴀᴅᴊᴜsᴛ sᴘᴇᴇᴅ • ᴄʜᴀɴɢᴇ ᴘʟᴀʏʙᴀᴄᴋ sᴘᴇᴇᴅ ɪɴ ɢʀᴏᴜᴘ"),
    BotCommand("cspeed", "❖ ᴄʜᴀɴɴᴇʟ sᴘᴇᴇᴅ • ᴀᴅᴊᴜsᴛ sᴘᴇᴇᴅ ɪɴ ᴄʜᴀɴɴᴇʟ"),
    BotCommand("tagall", "❖ ᴛᴀɢ ᴀʟʟ • ᴍᴇɴᴛɪᴏɴ ᴇᴠᴇʀʏᴏɴᴇ ɪɴ ɢʀᴏᴜᴘ"),
]

async def setup_bot_commands():
    try:
        await app.set_bot_commands(COMMANDS)
        LOGGER("AjnabiMusic").info("Bot commands set successfully!")
        
    except Exception as e:
        LOGGER("AjnabiMusic").error(f"Failed to set bot commands: {str(e)}")

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()

    await sudo()

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass

    await app.start()
    
    await setup_bot_commands()

    for all_module in ALL_MODULES:
        importlib.import_module("AjnabiMusic.plugins" + all_module)

    LOGGER("AjnabiMusic.plugins").info("Successfully Imported Modules...")

    await userbot.start()
    await Nand.start()

    try:
        await Nand.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("AjnabiMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass

    await Nand.decorators()

    LOGGER("AjnabiMusic").info(
        "\x53\x68\x72\x75\x74\x69\x20\x4d\x75\x73\x69\x63\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e\x0a\x0a\x44\x6f\x6e\x27\x74\x20\x66\x6f\x72\x67\x65\x74\x20\x74\x6f\x20\x76\x69\x73\x69\x74\x20\x40\x53\x68\x72\x75\x74\x69\x42\x6f\x74\x73"
    )

    await idle()

    await app.stop()
    await userbot.stop()
    LOGGER("AjnabiMusic").info("Stopping Ajnabi Music Bot...🥺")

if __name__ == "__main__":
    # ✅ RENDER FIX - YEH TARIKA SAHI KAAM KAREGA
    try:
        asyncio.run(init())
    except KeyboardInterrupt:
        LOGGER("AjnabiMusic").info("Bot stopped by user")
    except Exception as e:
        LOGGER("AjnabiMusic").error(f"Fatal error: {e}")


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots
