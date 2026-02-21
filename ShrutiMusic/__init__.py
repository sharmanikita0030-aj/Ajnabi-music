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


# ↓↓↓ SIRF YE 6 LINES MEIN ShrutiMusic → AjnabiMusic KARNA HAI ↓↓↓

from AjnabiMusic.core.bot import Nand          # Line 21: ShrutiMusic → AjnabiMusic
from AjnabiMusic.core.dir import dirr          # Line 22: ShrutiMusic → AjnabiMusic
from AjnabiMusic.core.git import git           # Line 23: ShrutiMusic → AjnabiMusic
from AjnabiMusic.core.userbot import Userbot   # Line 24: ShrutiMusic → AjnabiMusic
from AjnabiMusic.misc import dbb, heroku       # Line 25: ShrutiMusic → AjnabiMusic

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Nand()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic        # YAHAN KUCH MAT BADAL (original rahega)
# 📢 Telegram Channel : https://t.me/ShrutiBots           # YAHAN KUCH MAT BADAL (original rahega)
# ===========================================


# ❤️ Love From ShrutiBots
