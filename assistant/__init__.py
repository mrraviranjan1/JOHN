# JOHN - UserBot
# Copyright (C) 2021 TeamJOHN
#
# This file is a part of < https://github.com/mrraviranjan1/JOHN/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrraviranjan1/JOHN/blob/main/LICENSE/>.

from pyJOHN import *
from pyJOHN.functions.helper import *
from pyJOHN.misc import owner_and_sudos
from pyJOHN.misc._assistant import asst_cmd, callback, in_pattern
from telethon import Button, custom

from plugins import ATRA_COL
from strings import get_languages, get_string, language

OWNER_NAME = JHON_bot.me.first_name
OWNER_ID = JHON_bot.me.id

AST_PLUGINS = {}


async def setit(event, name, value):
    try:
        udB.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    return [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
