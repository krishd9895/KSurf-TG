from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")


class Telegram:
    API_ID = int(getenv("API_ID"))
    API_HASH = getenv("API_HASH")
    BOT_TOKEN = getenv("BOT_TOKEN")
    MULTI_TOKEN1 = getenv("MULTI_TOKEN1")
    
    PORT = int(getenv("PORT", "8180"))
    BASE_URL = getenv("BASE_URL").rstrip('/')
    DATABASE_URL = getenv("DATABASE_URL")
    AUTH_CHANNEL = [channel.strip()
                    for channel in getenv("AUTH_CHANNEL").split(",")]
    THEME = getenv("THEME", "quartz")
    USERNAME = getenv("USERNAME", "admin")
    PASSWORD = getenv("PASSWORD", "admin")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "surfTG")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "surfTG")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = bool(getenv('MULTI_CLIENT', 'False'))
