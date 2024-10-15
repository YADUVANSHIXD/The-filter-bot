import re
from os import environ,getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '29728878'))
API_HASH = environ.get('API_HASH', 'a961168f7807061e77e1fb39c3f6ef71')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://te.legra.ph/file/b4a3747fc57c0a78b8ce7.jpg https://te.legra.ph/file/96bfa2b897869b53f3c1b.jpg https://telegra.ph/file/ab7c45feabcd446799ec9.jpg https://telegra.ph/file/be0e05a69125057f7403d.jpg https://telegra.ph/file/083d98858adfc45ce1761.jpg https://telegra.ph/file/c3e7e855f6fe2deb7fe21.jpg https://telegra.ph/file/966dae7b6f91a58aa037c.jpg https://telegra.ph/file/fa74ca254cc4368c167cd.jpg https://telegra.ph/file/08e2e68f2d9c959ca30fc.jpg https://telegra.ph/file/1d63c8f8102d8bf6dd90f.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e20b5fdaf217252964202.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/70c306053d29595749a52.mp4")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/9f3f47c690bbcc67633c2.jpg'))
SUBSCRIPTIO = (environ.get('SUBSCRIPTION', 'https://graph.org/file/453630052fef8854ec138.jpg')).split()
CODE = (environ.get('CODE', 'https://te.legra.ph/file/0a702f3845e3462650366.jpg'))
PAYPICS = (environ.get('PAYPICS', 'https://te.legra.ph/file/a4770bb04f994e165ea80.jpg')).split()
REFER_PICS = (environ.get("REFER_PICS", "https://graph.org/file/1a2e64aee3d4d10edd930.jpg")).split() 

#stream link shortner
STREAM_SITE = (environ.get('STREAM_SITE', 'ziplinker.net')) # not support
STREAM_API = (environ.get('STREAM_API', '9d34b267ed4000cf536103bfec31a7a096ff4973'))
STREAMHTO = (environ.get('STREAMHTO', ''))
BOT_USERNAME = environ.get("BOT_USERNAME", "TheMovieFilterBot")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5294914915 7033385522').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002150820537 -1002235533210').split()] #Channel id for auto indexing ( make sure bot is admin )
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '7262773477 5294914915 7033385522').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '7262773477').split()]
auth_channel = environ.get('AUTH_CHANNEL', '') #Channel / Group Id for force sub ( make sure bot is admin )
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002041612661') # support group id ( make sure bot is admin )
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002107375884') # request channel id ( make sure bot is admin )
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')


#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '-1002170373025').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @B4UMovieHouse</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Others
VERIFY = bool(environ.get('VERIFY', True))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'instantearn.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '1dacaa27ce824e44b95f1b6a11939575205d1fa9')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/B4UMOVIEZONE')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/YADUVANSHIXBOTZ')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/How_to_open_movielink')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', 'ᴛʜᴀɴᴋ ʏᴏᴜ 💖ᴘʀᴀᴅᴇᴇᴘ💖')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002179479692')) #Log channel id ( make sure bot is admin )
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/YaduvanshiXsupport') #Support group link ( make sure bot is admin )
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", ""]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]
PREFIX = environ.get("PREFIX", "/")
# Online Stream and Download
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', 'rigid-ofella-movieboot-cd56b895.koyeb.app' ''))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "https://{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'JisshuBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'pradeep'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',True))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)


# Online Stream and Download
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or Flase

# online Stream and Download support only premium user, True or Flase
JS_WEB_PREMIUM = is_enabled((environ.get('JS_WEB_PREMIUM', "False")), False)

# website themes changing (https://bootswatch.com)
JS_THEMES = "cerulean"

# add premium logs channel id
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002172154834'))

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
