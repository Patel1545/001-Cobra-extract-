# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "29267685"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "9aea863501d41261e6c75ad565b6e1e1")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7783629621:AAFuMRVknpklqmGN5lT6Md8NJO3BCMADHCc")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@Cobra56_bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "7916516048"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7916516048", "-1002422196254").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002422196254"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srvter")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002422196254"))

