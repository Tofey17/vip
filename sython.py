import telethon
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import base64
import datetime
from payment import *
from help import *
from checktele import *
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
# -

sython.start()
c = requests.session()
bot_username = '@EEObot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@Ershkalibot'

y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy}"
sec = time.time()

LOGS = logging.getLogger(__name__)

DEVS = [
    6799580948,
]
DEL_TIME_OUT = 10
normzltext = "1234567890"
namerzfont = normzltext
name = "Profile Photos"
time_name = ["off"]
time_bio = ["off"]


async def join_channel():
    try:
        await sython(JoinChannelRequest("@zzsszzz"))
    except BaseException:
        pass




@sython.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
async def _(event):
    await event.edit(commands)

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
**☆ WELCOME TO TNT
☆ VERSION : 2.1
☆ PING : `{ms}`
☆ DATE : `{m9zpi}`
☆ ID : `{event.sender_id}`
☆ SOURCE BDthon : @BDthon**

-قـم بأرسال `.الاوامر`
''')


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.م1"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec1)


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.م2"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec2)


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.م3"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec3)


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.م4"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec4)
    
ownerhson_id = 6799580948
@sython.on(events.NewMessage(outgoing=False, pattern='/start'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('مرحبا ايها المطور')

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def update(event):
    await event.edit("• جارِ اعادة تشغيل السورس ..\n• انتضر 1-2 دقيقة  .")
    await sython.disconnect()
    await sython.send_message("me", "`اكتملت اعادة تشغيل السورس !`")

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython.get_entity(bot_username)
        await sython.send_message('@EEObot', 'جاري التجميع بواسطة | 𝗦𝗢𝗨𝗥𝗖𝗘 𝗕𝗗𝗧𝗛𝗢𝗡')
        channel_entity = await sython.get_entity(bot_username)
        await sython.send_message('@EEObot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython.get_messages('@EEObot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython.get_messages('@EEObot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython(ImportChatInviteRequest(bott))
                msg2 = await sython.get_messages('@EEObot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython.send_message(event.chat_id, "تم الانتهاء من التجميع !")


##################
@sython.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع ارشقلي"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython.get_entity(bot_usernameee)
        await sython.send_message('@Ershkalibot', 'جاري التجميع بواسطة | 𝗦𝗢𝗨𝗥𝗖𝗘 𝗕𝗗𝗧𝗛𝗢𝗡')
        channel_entity = await sython.get_entity(bot_usernameee)
        await sython.send_message('@Ershkalibot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython.get_messages('@Ershkalibot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython.get_messages('@Ershkalibot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython(ImportChatInviteRequest(bott))
                msg2 = await sython.get_messages('@Ershkalibot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython.send_message(event.chat_id, "تم الانتهاء من التجميع !")
        

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع الجوكر"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython.get_entity(bot_usernamee)
        await sython.send_message('@A_MAN9300BOT', 'جاري التجميع بواسطة | 𝗦𝗢𝗨𝗥𝗖𝗘 𝗕𝗗𝗧𝗛𝗢𝗡')
        channel_entity = await sython.get_entity(bot_usernamee)
        await sython.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython(ImportChatInviteRequest(bott))
                msg2 = await sython.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython.send_message(event.chat_id, "تم الانتهاء من التجميع !")

LOGS = logging.getLogger(__name__)

logging.basicConfig(
    format="[%(levelname)s- %(asctime)s]- %(name)s- %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)

async def join_channel():
    try:
        await sython(JoinChannelRequest("@zzsszzz"))
    except BaseException:
        pass
 
 
GCAST_BLACKLIST = [
    -1001884452589,
    -1001884452589,
]

DEVS = [
    6799580948,
]

def calc(num1, num2, fun):
    if fun == "+":
        return num1 + num2
    elif fun == "-":
        return num1 - num2
    elif fun == "*":
        return num1 * num2
    elif fun == "X":
        return num1 * num2
    elif fun == "x":
        return num1 * num2
    elif fun == "/":
        return num1 / num2
    elif fun == "÷":
        return num1 / num2
    else:
        return "خطأ"


@sython.on(events.NewMessage(outgoing=True, pattern=".احسب (.*)"))
async def _(event):
    try:
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        num1 = int(msg[0])
        num2 = int(msg[2])
        fun = str(msg[1])
        await event.edit(f''' الناتج = `{calc(num1, num2, fun)}`''')
    except:
        await event.edit('''خطأ, يرجى ادخال الرقم مثل :
7 + 7
7 - 7
7 x 7
7 ÷ 7''')


@sython.on(events.NewMessage(outgoing=True, pattern=".للكروبات(?: |$)(.*)"))
async def gcast(event):
    sython = event.pattern_match.group(1)
    if sython:
        msg = sython
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "**⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await event.edit("⌔∮ يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔∮  تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )


@sython.on(events.NewMessage(outgoing=True, pattern=".للخاص(?: |$)(.*)"))
async def gucast(event):
    sython = event.pattern_match.group(1)
    if sython:
        msg = sython
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "**⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await event.edit("⌔∮ يتم الاذاعة في الخاص انتظر لحضه")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔∮  تم بنجاح الأذاعة الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**"
    )

@sython.on(events.NewMessage(outgoing=True, pattern=".تكرار (.*)"))
async def spammer(event):
    sandy = await event.get_reply_message()
    cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(cat[0])
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    await spam_function(event, sandy, cat, sleeptimem, sleeptimet)


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):

    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await _catutils.unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass


@sython.on(events.NewMessage(outgoing=True, pattern=".مؤقت (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)
  
 
    
@sython.on(events.NewMessage(outgoing=True, pattern=".سورس"))
async def _(event):
      await event.reply("""السـورس يعمـل | 𝗦𝗢𝗨𝗥𝗖𝗘 𝗕𝗗𝗧𝗛𝗢𝗡
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

- المطور : توفي العامري

- سورس بسيط يحتوي على الاوامر المهمة التي تحتاجها

قناة السورس : @BDthon
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍"""
)

@sython.on(events.NewMessage(outgoing=True, pattern=".مطور"))
async def _(event):
      await event.edit("""تـــوفـــي الــعــامري الــديــكم لاخــوف عــلــعــلــيــكم
𖥔 ࣪ ˖🩸𖥔 ࣪ ˖💢 𖥔 ࣪ ˖💀𖥔 ࣪ ˖🕸𖥔 ࣪ ˖🪦𖥔 ࣪
قناه رسميه للمطور - @T33TD
قناه رسميه للسورس - @BDthon
𖥔 ࣪ ˖🩸𖥔 ࣪ ˖💢 𖥔 ࣪ ˖💀𖥔 ࣪ ˖🕸𖥔 ࣪ ˖🪦𖥔 ࣪"""
)

@sython.on(events.NewMessage(outgoing=True, pattern=".مصه"))
async def _(event):
      await event.edit("""
⣠⡶⠚⠛⠲⢄⡀
⣼⠁      ⠀⠀⠀⠳⢤⣄
⢿⠀⢧⡀⠀⠀⠀⠀⠀⢈⡇
⠈⠳⣼⡙⠒⠶⠶⠖⠚⠉⠳⣄
⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄
⠀⠀⠀⠘⣆       ⠀⠀⠀⠀⠀⠈⠓⢦⣀
⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤
⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧
⠀⠀⠀⠀⠀⠀⠀    ⠓⠦⠀⠀⠀⠀
🗿 ¦ تعال مصه عزيزي ࣪"""
)
@sython.on(events.NewMessage(outgoing=True, pattern=".حلويات"))
async def _(event):
    event = await event.edit("candy")
    deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))
    for _ in range(100):
        await asyncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)

@sython.on(events.NewMessage(outgoing=True, pattern=".قلوب"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("🖤")
    animation_chars = [
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

@sython.on(events.NewMessage(outgoing=True, pattern=".العد التنازلي"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("🔟")
    animation_chars = [
        "9️⃣",
        "8️⃣",
        "7️⃣",
        "6️⃣",
        "5️⃣",
        "4️⃣",
        "3️⃣",
        "2️⃣",
        "1️⃣",
        "0️⃣",
        "🆘",

    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

        
@sython.on(events.NewMessage(outgoing=True, pattern=".قمر"))
async def _(event):
    event = await event.edit("قمر")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)
        
@zedub.zed_cmd(pattern=".سيرفر")
async def _(event):
    animation_interval = 2
    animation_ttl = range(10)
    event = await edit_or_reply(event, "Power On......")
    animation_chars = [
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 10%\n\n    ●○○○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 5.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.13GB\n    **🔹used:** 33.77GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 158.98GB\n    **🔹recv:** 146.27GB\n    **🔹sent_packets:** 84518799\n    **🔹recv_packets:** 159720314\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 30%\n\n    ●●●○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 20.4%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 7.18GB\n    **🔹used:** 28.26GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 146.27GB\n    **🔹recv:** 124.33GB\n    **🔹sent_packets:** 54635686\n    **🔹recv_packets:** 143565654\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 60%\n\n    ●●●●●●○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 60.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 6.52GB\n    **🔹used:** 35.78GB\n    **🔹total:** 60.0GB\n    \n    ●●●○○○○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 124.33GB\n    **🔹recv:** 162.48GB\n    **🔹sent_packets:** 25655655\n    **🔹recv_packets:** 165289456\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 100%\n\n    ●●●●●●●●●●\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 100.0%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 9.81GB\n    **🔹used:** 30.11GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 162.48GB\n    **🔹recv:** 175.75GB\n    **🔹sent_packets:** 56565435\n    **🔹recv_packets:** 135345655\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 70%\n\n    ●●●●●●●○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 80.4%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 5.76GB\n    **🔹used:** 29.35GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 175.75GB\n    **🔹recv:** 118.55GB\n    **🔹sent_packets:** 36547698\n    **🔹recv_packets:** 185466554\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 60%\n\n    ●●●●●●○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 62.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.23GB\n    **🔹used:** 33.32GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 118.55GB\n    **🔹recv:** 168.65GB\n    **🔹sent_packets:** 24786554\n    **🔹recv_packets:** 156745865\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 30%\n\n    ●●●○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 30.6%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 9.75GB\n    **🔹used:** 36.54GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 168.65GB\n    **🔹recv:** 128.35GB\n    **🔹sent_packets:** 56565435\n    **🔹recv_packets:** 1475823589\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 10%\n\n    ●○○○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 10.2%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 10.20GB\n    **🔹used:** 25.40GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 128.35GB\n    **🔹recv:** 108.31GB\n    **🔹sent_packets:** 54635686\n    **🔹recv_packets:** 157865426\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 100%\n\n    ●●●●●●●●●●\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 100.0%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 5.25GB\n    **🔹used:** 31.14GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 108.31GB\n    **🔹recv:** 167.17GB\n    **🔹sent_packets:** 84518799\n    **🔹recv_packets:** 124575356\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 70%\n\n    ●●●●●●●○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 76.2%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.01GB\n    **🔹used:** 33.27GB\n    **🔹total:** 60.0GB\n    \n    ●●●○○○○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 167.17GB\n    **🔹recv:** 158.98GB\n    **🔹sent_packets:** 36547698\n    **🔹recv_packets:** 165455856\n\n\n**===================**\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])
        
@sython.on(events.NewMessage(outgoing=True, pattern=".قمور"))
async def _(event):
    event = await event.edit("قمور")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("قمور..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])






print("- sython Userbot Running ..")
sython.run_until_disconnected()
