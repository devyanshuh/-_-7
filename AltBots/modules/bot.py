import sys
import heroku3

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl

from os import execl, getenv
from telethon import events
from datetime import datetime


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        altron = await e.reply(f"•[ 🍹𝘞𝘈𝘙 𝘔𝘈𝘊𝘏𝘐𝘕𝘌🍹 ]•")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit( ⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️
⚡️𝑾𝑨𝑹 ✗ 𝑫𝑨𝑫𝑫𝒀 ⚡️
⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️
⚡️𝑹𝑬𝑨𝑫𝒀 𝑻𝑶 𝑭𝑪𝑲⚡️
⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️➜ `{mp} ms`")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"𝘙𝘦𝘣𝘰𝘰𝘵 𝘥𝘰𝘯𝘦\n[🍷] 2 𝘮𝘪𝘯 𝘸𝘢𝘪𝘵 𝘱𝘭𝘦𝘢𝘴𝘦\n[🫧] 𝘧𝘪𝘳 𝘢𝘢𝘶𝘯𝘨𝘢 𝘵𝘶𝘫𝘩𝘦 𝘤𝘩𝘰𝘥𝘯𝘦")
        try:
            await X1.disconnect()
        except Exception:
            pass
        try:
            await X2.disconnect()
        except Exception:
            pass
        try:
            await X3.disconnect()
        except Exception:
            pass
        try:
            await X4.disconnect()
        except Exception:
            pass
        try:
            await X5.disconnect()
        except Exception:
            pass
        try:
            await X6.disconnect()
        except Exception:
            pass
        try:
            await X7.disconnect()
        except Exception:
            pass
        try:
            await X8.disconnect()
        except Exception:
            pass
        try:
            await X9.disconnect()
        except Exception:
            pass
        try:
            await X10.disconnect()
        except Exception:
            pass

        execl(sys.executable, sys.executable, *sys.argv)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply(f"»🍃 𝘔𝘌𝘙𝘈 𝘌𝘒 𝘕𝘌𝘞 𝘉𝘌𝘛𝘈 𝘈𝘋𝘋 𝘏𝘖𝘎𝘠𝘈 🍃")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("𝘈𝘉𝘌 𝘑𝘏𝘈𝘛 𝘒𝘌 𝘉𝘈𝘈𝘓 𝘜𝘗𝘈𝘙 𝘚𝘈𝘐 𝘙𝘌𝘗𝘓𝘠 𝘋𝘌𝘙𝘏𝘈 𝘉𝘈𝘈𝘗 𝘒𝘖")
            return

        if str(target) in sudousers:
            await ok.edit(f"ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !!")
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit(f"» 𝘖𝘠𝘌 𝘏𝘖𝘠𝘌 𝘞𝘈𝘙 𝘒𝘈 𝘕𝘌𝘞 𝘉𝘌𝘛𝘈\n:⧽ `{target}`\n:⧽ 𝘞𝘌𝘓𝘊𝘖𝘔𝘌 𝘛𝘖 𝘞𝘈𝘙 𝘔𝘈𝘊𝘏𝘐𝘕𝘌")
            heroku_var["SUDO_USERS"] = newsudo    
    
    elif event.sender_id in SUDO_USERS:
        await event.reply("» ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
