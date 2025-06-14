import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", ))
    API_HASH = os.environ.get("API_HASH", "")
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", ""))
    
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    UPDATES_CHANNEL_USERNAME = os.environ.get("UPDATES_CHANNEL_USERNAME", "")
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    RESULTS_COUNT = int(os.environ.get("RESULTS_COUNT", 5))
    BROADCAST_AS_COPY = os.environ.get("BROADCAST_AS_COPY", "True")
    
    MOVIE_WEBSITE = os.environ.get("MOVIE_WEBSITE", "")
    FORCE_SUB = os.environ.get("FORCE_SUB", "True")
    AUTO_DELETE_TIME = int(os.environ.get("AUTO_DELETE_TIME", 300))
    MDISK_API = os.environ.get("MDISK_API", "12334")

    REPLIT_USERNAME = os.environ.get("REPLIT_USERNAME", "")
    REPLIT_APP_NAME = os.environ.get("REPLIT_APP_NAME", "")
    REPLIT = f"https://{REPLIT_APP_NAME.lower()}.{REPLIT_USERNAME}.repl.co" if REPLIT_APP_NAME and REPLIT_USERNAME else False

    PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))

    ABOUT_BOT_TEXT = """<b>This is ShareDisk Movie Search Bot.

🤖 My Name: <a href='https://t.me/iPopcornMovieBot'>i Popcorn Movie Bot</a>

📝 Language : <a href='https://www.python.org'>Python V3</a>

📚 Library: <a href='https://docs.telethon.org'>Telethon</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/RoyalKrrishna'>Royal Krrishna</a></b>
"""

    ABOUT_HELP_TEXT = """
<b>
👨‍💻 Developer : <a href='https://t.me/keshavraj_77'>keshav bhai</a></b>
"""

    HOME_TEXT = """
Iꜰ Yᴏᴜ Lɪᴋᴇ Mᴇ!😘

Pʟᴇᴀꜱᴇ Sʜᴀʀᴇ Mᴇ Wɪᴛʜ Yᴏᴜʀ 
Fʀɪᴇɴᴅꜱ Aɴᴅ Fᴀᴍɪʟʏ.👨‍👨‍👧

Mᴀᴅᴇ Wɪᴛʜ ❤ Bʏ @keshavraj_77
"""

    START_MSG = """
**Hᴇʏ! {}😅,

Mᴇ! SʜᴀʀᴇDɪꜱᴋ Mᴏᴠɪᴇ Sᴇᴀʀᴄʜ Bᴏᴛ.🤖

I Cᴀɴ Sᴇᴀʀᴄʜ Mᴏᴠɪᴇꜱ Fᴏʀ Yᴏᴜ.🔍

Mᴀᴅᴇ Wɪᴛʜ ❤ Bʏ @keshavraj_77**
"""
