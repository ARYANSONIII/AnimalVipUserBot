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
from STORM.Database.pm import *
from STORM.powers import get_id
from config import PM_PIC, SUDO_USERS
hl = "."
pm_watcher = 5
KEX = PM_PIC

TEXT = """
•            **[𝖣𝗋. 𝖲𝗈𝗇𝖺𝗅 𝖯𝗋𝗈𝗈𝖿𝗌](https://t.me/)**
╰• **𝖣𝗋. 𝖲𝗈𝗇𝖺𝗅** » {}
• **🛡️ 𝖳𝗁𝗂𝗌 𝗂𝗌 𝖺 𝖣𝗋. 𝖲𝗈𝗇𝖺𝗅 𝖯𝗋𝗂𝗏𝖺𝖼𝗒 🛡️**
➖➖➖➖➖➖➖➖➖➖➖ 
    **𝖧𝖾𝗒 𝖡𝗎𝖽𝖽𝗒** 
    **𝖥𝗂𝗋𝗌𝗍 𝖸𝗈𝗎 𝗐𝗂𝗅𝗅 𝖻𝖾 𝗉𝖺𝗒 50 𝖱𝗌.**
    **𝖠𝖿𝗍𝖾𝗋 𝖯𝖺𝗒 𝗌𝖾𝗇𝖽 𝖲𝖼𝗋𝖾𝖾𝗇𝗌𝗁𝗈𝗍 𝖧𝖾𝗋𝖾**
    **𝖳𝗁𝖾𝗇 𝖸𝗈𝗎 𝖼𝖺𝗇 𝗀𝖾𝗍 𝖱𝖾𝗉𝗅𝗒 𝖿𝗋𝗈𝗆 𝗆𝗒 𝖲𝗂𝖽𝖾**
    **𝖭𝗈 𝖺𝗇𝗒 𝖲𝗉𝖺𝗆 𝖧𝖾𝗋𝖾** 
    **𝖮𝗍𝗁𝖾𝗋𝗐𝗂𝗌𝖾 𝖸𝗈𝗎 𝗐𝗂𝗅𝗅 𝖻𝖾 𝖡𝗅𝗈𝖼𝗄𝖾𝖽**
• **𝖶𝖺𝗋𝗇 𝖫𝗂𝗆𝗂𝗍𝗌** » {}      
╰• **𝖸𝗈𝗎𝗋 𝖶𝖺𝗋𝗇𝗌** » {}
➖➖➖➖➖➖➖➖➖➖➖
•           **[𝖣𝗋. 𝖲𝗈𝗇𝖺𝗅 𝖯𝗋𝗈𝗈𝖿𝗌](https://t.me/)**
"""

@Client.on_message(
    filters.command(["pmpermit"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def pmpermit(client, message):
    x = await is_pm_on()
    try:
        tg = message.text.split()[1].lower()
    except:
        return await message.edit(f"{hl}pmpermit [on | off]")
    if not tg in ["on", "off"]:
        return await message.edit(f"{hl}pmpermit [on | off]")
    if tg == "on":
        if x:
            return await message.edit("ᴘᴍᴘᴇʀᴍɪᴛ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ....")
        await toggle_pm()
        if await limit() == 0:
            await update_warns(3)
        return await message.edit("ᴘᴍᴘᴇʀᴍɪᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴇɴᴀʙʟᴇᴅ....")
    if not x:
        return await message.edit("ᴘᴍᴘᴇʀᴍɪᴛ ɪꜱ ɴᴏᴛ ᴇɴᴀʙʟᴇᴅ....")
    await toggle_pm()
    return await message.edit("ᴘᴍᴘᴇʀᴍɪᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅɪꜱᴀʙʟᴇᴅ....")

@Client.on_message(
    filters.command(["approve", "disapprove", "a", "da", "allow", "disallow"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def appr_dis(client, message):
    if str(message.chat.id)[0] == "-":
        try:
            id = await get_id(_, message)
        except:
            return await message.edit("ꜰᴏʀ ᴀᴘᴘʀᴏᴠᴇ ᴜꜱᴇʀ ɪɴ ɢʀᴏᴜᴘ ᴜ ᴡᴀɴᴛ ᴛᴏ ɢɪᴠᴇ ᴍᴇ ɪ'ᴅ ᴏʀ ʀᴇᴘʟʏ ᴛʜᴀᴛ ᴜꜱᴇʀ..")
    else:
        id = message.chat.id
    tg = message.text.split()[0][1]
    x = await is_approved(id)
    if tg == "d":
        if not x:
            return await message.edit("ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ɴᴏᴛ ᴀᴘᴘʀᴏᴠᴇᴅ..")
        await disapprove(id)
        return await message.edit("ᴜꜱᴇʀ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅɪꜱᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ....")
    if x:
        return await message.edit("ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ ᴜꜱᴇʀ ᴀʟʀᴇᴀᴅʏ ᴀᴘᴘʀᴏᴠᴇᴅ....")
    await approve(id) 
    await reset_warns(id)
    return await message.edit("ᴜꜱᴇʀ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ....")

@Client.on_message(
    filters.command(["setwarns"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def setwarn(client, message):
    try:
        count = int(message.text.split()[1])
    except:
        return await message.edit(f"{hl}setwarns [ᴠᴀʟᴜᴇ]")
    if count == 0:
        return await message.edit("ɢɪᴠᴇ ᴍᴇ ᴠᴀʟᴜᴇ ᴛᴏ ꜱᴇᴛ ᴡᴀʀɴꜱ..")
    await update_warns(count)
    await message.edit(f"ᴅᴍ ᴡᴀʀɴꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜱᴇᴛ ᴛᴏ {count}..")
    
@Client.on_message(filters.private, group=pm_watcher)
async def wtch(client, message):
    user_ = message.from_user
    if message.from_user.id == client.me.id:
        return
    if not await is_pm_on():
        return
    if user_.is_bot:
        return
    if await is_approved(message.from_user.id):
        return
    await add_warn(message.from_user.id)
    if await limit() <= await get_warns(message.from_user.id):
        await message.reply("ꜱᴘᴀᴍᴍᴇʀ ᴅᴇᴛᴇᴄᴛᴇᴅ ᴀɴᴅ ʙʟᴏᴄᴋᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ.....")
        await reset_warns(message.from_user.id)
        return await client.block_user(message.from_user.id)
    await message.reply_photo(KEX, caption=TEXT.format((await client.get_me()).first_name, await limit(), await get_warns(message.from_user.id)))
