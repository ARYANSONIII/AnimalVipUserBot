#MIT License

#Copyright (c) 2024 ᴋᴜɴᴀʟ [AFK]

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from pyrogram import Client, filters
from config import SUDO_USERS

@Client.on_message(
    filters.command(["repo"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def repo(client, message):
    msg = f"""
    ** ᴀɴɪᴍᴀʟ ᴜꜱᴇʀʙᴏᴛ **

    • **ɢɪᴛʜᴜʙ** » [click here](https://te.legra.ph/file/ec19cf227791a167abedc.jpg) 
    • **ꜱᴜᴘᴘᴏʀᴛ** » [click here](https://t.me/tabahi_tabahi) 
    • **ᴜᴘᴅᴀᴛᴇꜱ** » [click here](https://t.me/knight_society)
    • **ᴅᴇᴠᴇʟᴏᴘᴇʀ** » [click here](https://t.me/smartness_to_hai)
    
    **ʙʏ @smartness_to_hai**
    """
    await message.edit(msg)
