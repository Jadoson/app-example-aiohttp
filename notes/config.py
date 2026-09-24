import os

HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", 8080))
APP_TITLE = os.environ.get("APP_TITLE", "Заметки")
