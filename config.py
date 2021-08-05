import os


class Config:
    API_ID = "1575454" #int(os.environ.get("API_ID"))
    API_HASH = "66a82fd51b50e02c604e7253b8e27572" #os.environ.get("API_HASH")
    AUTH_USERS = "209544830" #set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    BOT_TOKEN = "1926247211:AAEQqqprWT4buCS0yBQt5ggJnn2pdk7y_5c" #os.environ.get("BOT_TOKEN")
    DB_URI = os.environ.get("DATABASE_URL")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    SESSION_NAME = "MediaInfo_RoBot" #os.environ.get("SESSION_NAME")
    WORKERS = 200
