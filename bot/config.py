import os


class Config:

    BOT_TOKEN = os.environ.get("1661344544:AAG-VdZcC1R18-qyWqDUJbIUN7zc0uGC_L0")

    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")

    API_ID = int(os.environ.get("5036031"))

    API_HASH = os.environ.get("d1a9a1d406988ee1c988c1e767a5696c")

    CLIENT_ID = os.environ.get("932591237758-tn6oqcr49lgpqtcip1idlskcve4540nc.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("TH1Pu3iYPAE45Qy3Z5nYpibp")

    BOT_OWNER = int(os.environ.get("1015669446"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
