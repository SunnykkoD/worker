#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("6432787208:AAHYz78Ur4d02PM3PJWEPjN_wu_1v_aEBjQ", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("26091143", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("d5607263370062596af9037fa4f66dff", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("-1002113922845", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("6152856449", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("mongodb+srv://rranimesp:123789Aa@cluster0.uu7gn3x.mongodb.net/?retryWrites=true&w=majority", "")
DB_NAME = os.environ.get("Cluster0", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("-1001427161064", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hola {first}\n\nSoy el bot que da los animes completos, ve a @rranimespHD y busca el anime que quieres.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hola {first}\n\n<b>Necesitas estar unido al canal para usarme.\n\nÚnete @rranimespHD</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Este bot solo proporciona, no es necesario que escriba. Busque el link en @rranimespHD"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
