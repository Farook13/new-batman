import re
from os import environ
from Script import script
import pytz

def is_enabled(type, value):
    data = environ.get(type, str(value))
    if data.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif data.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        print(f'Error - {type} is invalid, exiting now')
        exit()

def is_valid_ip(ip):
    ip_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.match(ip_pattern, ip) is not None

# Bot information
API_ID = environ.get('API_ID', '12618934')
if len(API_ID) == 0:
    print('Error - API_ID is missing, exiting now')
    exit()
else:
    API_ID = int(API_ID)
API_HASH = environ.get('API_HASH', '49aacd0bc2f8924add29fb02e20c8a16')
if len(API_HASH) == 0:
    print('Error - API_HASH is missing, exiting now')
    exit()
BOT_TOKEN = environ.get('BOT_TOKEN', '7693803634:AAFIWfW8gfzMYv-G5-I9hAnge1mYFVkspio')
if len(BOT_TOKEN) == 0:
    print('Error - BOT_TOKEN is missing, exiting now')
    exit()
PORT = int(environ.get('PORT', '8000'))

# Bot pics
PICS = (environ.get('PICS', ' https://graph.org/file/8ac9be0d690c03e4a6d58-052f8fcda4d18922b8.jpg https://envs.sh/t7j.jpg https://envs.sh/t7c.jpg  https://envs.sh/t7G.jpg https://envs.sh/t7L.jpg https://envs.sh/t7c.jpg https://envs.sh/t7_.jpg https://envs.sh/tzT.jpg ')).split()

# Bot Admins
ADMINS = environ.get('ADMINS', '5032034594')
if len(ADMINS) == 0:
    print('Error - ADMINS is missing, exiting now')
    exit()
else:
    ADMINS = [int(admins) for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = [int(index_channels) if index_channels.startswith("-") else index_channels for index_channels in environ.get('INDEX_CHANNELS','-1002470153670').split()]
if len(INDEX_CHANNELS) == 0:
    print('Info - INDEX_CHANNELS is empty')
LOG_CHANNEL = environ.get('LOG_CHANNEL', '-1002332361885')
if len(LOG_CHANNEL) == 0:
    print('Error - LOG_CHANNEL is missing, exiting now')
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)
FORCE_SUB_CHANNELS = [int(fsub_channels) if fsub_channels.startswith("-") else fsub_channels for fsub_channels in environ.get('FORCE_SUB_CHANNELS','-1002407207522').split()]
if len(FORCE_SUB_CHANNELS) == 0:
    print('Info - FORCE_SUB_CHANNELS is empty')
    
TARGET_RESPONSE_TIME = 0.2 
    
#  support group
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '-1002256041072')
if len(SUPPORT_GROUP) == 0:
    print('Error - SUPPORT_GROUP is missing, exiting now')
    exit()
else:
    SUPPORT_GROUP = int(SUPPORT_GROUP)

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://Skking49:Skking49@sktesting.awlap.mongodb.net/?retryWrites=true&w=majority&appName=Sktesting")
if len(DATABASE_URL) == 0:an.saw
    print('Error - DATABASE_URL is missing, exiting now')
    exit()
DATABASE_NAME = environ.get('DATABASE_NAME', "batman13")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/cine_flix01')
OWNER_USERNAME = environ.get("OWNER_USERNAME", "https://t.me/Farook13")
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/cine_flix01')
FILMS_LINK = environ.get('FILMS_LINK', 'https://t.me/cine_flix01')
TUTORIAL = environ.get("TUTORIAL", "https://t.me/HA_Bo")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/")

# Bot settings
TIME_ZONE = pytz.timezone(environ.get("TIME_ZONE", 'Asia/Colombo'))
DELETE_TIME = int(environ.get('DELETE_TIME', 3600)) # Add time in seconds
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
MAX_BTN = int(environ.get('MAX_BTN', 10))
LANGUAGES = [language.lower() for language in environ.get('LANGUAGES', 'hindi english telugu tamil kannada malayalam marathi punjabi').split()]
QUALITY = [quality.lower() for quality in environ.get('QUALITY', '360p 480p 720p 1080p 2160p').split()]
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "mdiskshortner.link")
SHORTLINK_API = environ.get("SHORTLINK_API", "36f1ae74ba1aa01e5bd73bdd0bc22aa915443501")
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]
PM_FILE_DELETE_TIME = int(environ.get('PM_FILE_DELETE_TIME', '3600'))

# boolean settings
IS_VERIFY = is_enabled('IS_VERIFY', False)
AUTO_DELETE = is_enabled('AUTO_DELETE', False)
WELCOME = is_enabled('WELCOME', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
LONG_IMDB_DESCRIPTION = is_enabled("LONG_IMDB_DESCRIPTION", False)
LINK_MODE = is_enabled("LINK_MODE", True)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IMDB = is_enabled('IMDB', False)
SPELL_CHECK = is_enabled("SPELL_CHECK", True)
SHORTLINK = is_enabled('SHORTLINK', False)

# for stream
IS_STREAM = is_enabled('IS_STREAM', True)
BIN_CHANNEL = environ.get("BIN_CHANNEL", "-1002289409354")
if len(BIN_CHANNEL) == 0:
    print('Error - BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "https://t.me/batmnnol")
if len(URL) == 0:
    print('Error - URL is missing, exiting now')
    exit()
else:
    if URL.startswith(('https://', 'http://')):
        if not URL.endswith("/"):
            URL += '/'
    elif is_valid_ip(URL):
        URL = f'http://{URL}/'
    else:
        print('Error - URL is not valid, exiting now')
        exit()

#start command reactions and sticker
# Multiple sticker can be used separated by space, use @idstickerbot for get sticker id

