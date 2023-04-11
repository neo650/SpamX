from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "SpamX"
pic = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/9827c9802c4c9a6ebbb8b.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "lalunalaluna"
# message = "❄️❄️ yayo ❄️❄️ \n 1g -> 15k \n dt reyk \n DROP A DM \n +3547644179"
message = "+3547644179"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
     
━───────╯•╰───────━

➠ YAYO REYKJAVÍK

❄️❄️  1g - 16k ISK  ❄️❄️
❄️❄️  2g - 30k ISK  ❄️❄️
❄️❄️  3g - 45k ISK  ❄️❄️

➠ CALL OR DM
{message} 

use Signal for faster response

➠ CALL OR DM
{message} 

➠ YAYO REYKJAVÍK

━───────╮•╭───────━

     """
     
#      msg = f"""
# **⁂ {amsg} ⁂**

# ━───────╯•╰───────━
# ➠ **Master:** {owner_mention}
# ➠ **Python Version:** `{platform.python_version()}`
# ➠ **SpamX Version:** `{__version__}`
# ➠ **Pyrogram Version:** `{pyro_vr}`
# ➠ **pyRiZoeLX Version:** `{pip_vr}`
# ➠ **Channel:** @RiZoeLX
# ━───────╮•╭───────━
#      """

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from SpamX.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser
