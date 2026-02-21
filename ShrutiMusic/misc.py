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


import socket
import time
import os

from pyrogram import filters

import config
from AjnabiMusic.core.mongo import mongodb   # ShrutiMusic → AjnabiMusic

from .logging import LOGGER

SUDOERS = filters.user()
HAPP = None   # Heroku ke liye tha, ab nahi use hoga
_boot_ = time.time()


def is_render():
    """Check if running on Render"""
    return "RENDER" in os.environ or "render" in socket.getfqdn()


def dbb():
    global db
    db = {}
    LOGGER(__name__).info(f"Local Database Initialized.")


async def sudo():
    global SUDOERS
    SUDOERS.add(config.OWNER_ID)
    sudoersdb = mongodb.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    if config.OWNER_ID not in sudoers:
        sudoers.append(config.OWNER_ID)
        await sudoersdb.update_one(
            {"sudo": "sudo"},
            {"$set": {"sudoers": sudoers}},
            upsert=True,
        )
    if sudoers:
        for user_id in sudoers:
            SUDOERS.add(user_id)
    LOGGER(__name__).info(f"Sudoers Loaded.")


# ⚠️ HEROKU PURE HATA DIYA - Render safe!
def heroku():
    """Heroku function disabled for Render safety"""
    if is_render():
        LOGGER(__name__).info(f"Running on Render - Heroku features disabled")
        return
    else:
        LOGGER(__name__).info(f"Not on Render, but Heroku support removed for safety")
        return


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots
