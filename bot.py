import os
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION")
Bot = Client(
    "MusicEditorBot",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)
User = Client(
    session_name=SESSION,
    api_id=API_ID,
    api_hash=API_HASH
)

START_TXT = """
Hi {}, I am Music Editor Bot.
I can change the music tags and artwork.

Send a music to get started.
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source Code', url='https://github.com/samadii/MusicEditorBot'),
        ]]
    )


@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

   
@Bot.on_message(filters.channel & filters.text)
async def tag(bot, message):
    m = message.text
    n = m.split(f" {m.rsplit(' ', 1)[1]}")[0]
    X = m.split(f" {m.rsplit(' ', 1)[1]}")[0]
    y = m.rsplit(' ', 1)[1]
    if message.text:
        Copyright = "Kurulus Osman & Yemin & Son Yaz & Bir Zamanlar Kibris & Kazara Ask & Sadakatsiz & Iste Bu Benim Masalim & Hukumsuz & Gonul Dagi & Yesilcam & Ada Masali & Askin Tarifi & Baht Oyunu & Akinci & Teskilat & Saygi"
        No_Copyright = "Masumlar Apartmani & Sen Cal Kapimi & Bir Zamanlar Cukurova & Mucize Doktor & Dunya Hali & Bas Belasi & Ikimizin Sirri & Kalp Yarasi & Uyanis Buyuk Selcuklu & Kardeslerim & Emanet & EDHO & Yasak Elma & Ask Mantik Intikam & Bozkir Arslani Celaleddin"

        Copy = set(x for x in Copyright.split(' & '))
        NoCopy = set(x for x in No_Copyright.split(' & '))
        msgid = None
        liink = None
        Dublink = None
        kanal = None
        kap = None
        kap2 = None

        # Banner List
        if "Dunya Hali" in m:
            msgid = 2
            kanal = -1001572947427
            liink = "https://t.me/joinchat/rXqnANpb4ddmYmQ0"
        if "Sen Cal Kapimi" in m:
            msgid = 3
            kanal = -1001499596110
            Dublink = "https://t.me/joinchat/djHUcZrf3Z1lMGFk"
            liink = "https://t.me/joinchat/AAAAAFliBU5b2xvHML3pKw"
        if "Bas Belasi" in m:
            msgid = 4
            kanal = -1001531011385
            liink = "https://t.me/joinchat/CHt9Qm2i7ddjMWNk"
        if "Ikimizin Sirri" in m:
            msgid = 5
            kanal = -1001532685962
            liink = "https://t.me/joinchat/PPE9Q0Trw_A3OWNk"
        if "Kalp Yarasi" in m:
            msgid = 6
            kanal = -1001288493498
            liink = "https://t.me/joinchat/ji3XBL9w3lUwOGU8"
        if "Uyanis Buyuk Selcuklu" in m:
            msgid = 7
            kanal = -1001171502880
            liink = "https://t.me/joinchat/AAAAAEXTtyDMXmk804DQSQ"
        if "Kardeslerim" in m:
            msgid = 8
            kanal = -1001395391486
            liink = "https://t.me/joinchat/InuGULJZjGQyNmY0"
        if "Emanet" in m:
            msgid = 9
            kanal = -1001270763452
            liink = "https://t.me/joinchat/AAAAAEu-T7wxLlMxliwJyw"
        if "Yasak Elma" in m:
            msgid = 11
            kanal = -1001239367474
            liink = "https://t.me/joinchat/AAAAAEnfPzLtPdGaXGMEzg"
        if "Ask Mantik Intikam" in m:
            msgid = 12
            kanal = -1001553912535
            liink = "https://t.me/joinchat/drN40_tQtfxhM2U0"
        if "Bir Zamanlar Cukurova" in m:
            msgid = 13
            kanal = -1001202280419
            liink = "https://t.me/joinchat/AAAAAEepV-MEDL0PP0ceQQ"
        if "Bozkir Arslani Celaleddin" in m:
            msgid = 14
            kanal = -1001587441079
            liink = "https://t.me/joinchat/kf7uh3Cq1bc1NDlk"
        if "EDHO" in m:
            msgid = 10
            kanal = -1001476598094
            liink = "https://t.me/joinchat/AAAAAFgDGU4Oh-eEV4LnRw"
        if "Mucize Doktor" in m:
            msgid = 37
            kanal = -1001346815849
            Dublink = "https://t.me/joinchat/P9gAggky76PbWSNG"
            liink = "https://t.me/joinchat/AAAAAFBGx2l-B8oY1cTbag"
        if "Akinci" in m:
            msgid = 30
            liink = "https://t.me/joinchat/VSCZ1_t7aF2IGPer"
        if "Teskilat" in m:
            msgid = 29
            liink = "https://t.me/joinchat/OxIJyjwjHjNlMGE0"
        if "Sadakatsiz" in m:
            msgid = 27
            liink = "https://t.me/joinchat/AAAAAFWnj9SBrHU-TrESBA"
        if "Baht Oyunu" in m:
            msgid = 15
            liink = "https://t.me/joinchat/mJW2DUgtK2I4NTc8"
        if "Gonul Dagi" in m:
            msgid = 24
            liink = "https://t.me/joinchat/AAAAAE172331Q2Zcumf_fg"
        if "Yemin" in m:
            msgid = 22
            liink = "https://t.me/joinchat/Hg0iLFonT7o0YjE0"
        if "Son Yaz" in m:
            msgid = 21
            liink = "https://t.me/joinchat/Sp5ApZRoHoye3pJe"
        if "Bir Zamanlar Kibris" in m:
            msgid = 19
            liink = "https://t.me/joinchat/ANEuc6YkrKAxN2Jk"
        if "Askin Tarifi" in m:
            msgid = 17
            liink = "https://t.me/joinchat/iy5rkCQ_KPpiZGE0"
        if "Yesilcam" in m:
            msgid = 20
            liink = "https://t.me/joinchat/8WqFLl-BjjhkYWU0"
        if "Eshghe Mashroot" in m:
            msgid = 36
            liink = "https://t.me/joinchat/djHUcZrf3Z1lMGFk"
        if "Ghermez" in m:
            msgid = 32
            liink = "https://t.me/joinchat/gxjiMKv7NRg0ZWI0"
        if "Saygi" in m:
            msgid = 28
        if "Ada Masali" in m:
            msgid = 16
        if "Iste Bu Benim Masalim" in m:
            msgid = 26
        if "Hukumsuz" in m:
            msgid = 25
        if "Be Eshghe To Sogand" in m:
            msgid = 35
            liink = "https://t.me/joinchat/WvQDR7-EQItkMjFk"
        if X == "Cukurova":
            msgid = 38
            liink = "https://t.me/joinchat/AAAAAFWu07lSP1xokkxQAQ"
        if "Alireza" in m:
            msgid = None
            liink = "https://t.me/joinchat/ZSbUcIaTW9UwYmFk"
        if "Aparteman Bigonahan" in m:
            msgid = 34
            liink = "https://t.me/joinchat/jH8N1M12K3A2ODY8"
        if "Masumlar Apartmani" in m:
            msgid = 34
            kanal = -1001492549082
            liink = "https://t.me/joinchat/WPZ92vFSbeyHJk-e"
            Dublink = "https://t.me/joinchat/jH8N1M12K3A2ODY8"
        if X == "2020":
            msgid = 31
            liink = "https://t.me/joinchat/0ShOWZms2mpjZjE8"
        if "Yek Jonun Yek Eshgh" in m:
            msgid = 33
            liink = "https://t.me/joinchat/05Yh16Cj_-UyNDA8"
        if "Mojeze Doctor" in m:
            msgid = 37
            liink = "https://t.me/joinchat/P9gAggky76PbWSNG"
        hash = '#' + f'{X.replace(" ", "_")}'
        if kanal is None:
            if (X in Copy) and (liink is None):
                kap = f"⬇️سریال {hash} ({fa.replace('#', '').replace('_', ' ') } ) ، بازیرنویس چسبیده \n✅ قسمت : {E}\n💢کل قسمت ها\n\n⬇️1080👉\n⬇️720👉\n⬇️480👉\n⬇️240👉\n\n🆔👉 @dlmacvin"
            elif (X in Copy) and (liink is not None):
                if Dublink is None:
                    kap = f"⬇️سریال {hash} ({fa.replace('#', '').replace('_', ' ') } ) ، بازیرنویس چسبیده \n✅ قسمت : {E}\n💢[کل قسمت ها]({liink})\n\n⬇️1080👉\n⬇️720👉\n⬇️480👉\n⬇️240👉\n\n🆔👉 @dlmacvin_new"
                if Dublink is not None:
                    kap = f"💢 سریال {fa.replace('#', '').replace('_', ' ') }\n💢[کل قسمت ها (دوبله فارسی)]({Dublink})\n💢[کل قسمت ها (زیرنویس چسبیده)]({liink})\n\n📦 تا قسمت {E} در کانال زیر اضافه شد👇👇👇\n{liink}\n\n🆔👉 @dlmacvin_new | {fa}"
            if (not X in Copy) and (liink is None):
                kap = f"⬇️سریال ({fa.replace('#', '').replace('_', ' ')} ) ، با دوبله فارسی \n✅تا قسمت {E}\n\n🆔👉 @dlmacvin_new"
            elif (not X in Copy) and (liink is not None):
                kap = f"⬇️سریال ({fa.replace('#', '').replace('_', ' ')} ) ، با دوبله فارسی \n✅تا قسمت {E}\n\n{liink}\n\n🆔👉 @dlmacvin_new"

        elif kanal is not None:
            
            if (Dublink is not None):
                kap = f"⬇️سریال {hash} ({fa.replace('#', '').replace('_', ' ') } ) ، بازیرنویس چسبیده \n✅ قسمت : {E}\n💢[کل قسمت ها]({liink})\n\n⬇️1080👉\n⬇️720👉\n⬇️480👉\n⬇️240👉\n\n🆔👉 @dlmacvin_new"
                # kap2 = f"💢 سریال {fa.replace('#', '').replace('_', ' ') }\n💢[کل قسمت ها (دوبله فارسی)]({Dublink})\n💢[کل قسمت ها (زیرنویس چسبیده)]({liink})\n\n📦 تا قسمت {E} در کانال زیر اضافه شد👇👇👇\n{liink}\n\n🆔👉 @dlmacvin_new | {fa}"
            elif (Dublink is None):
                kap = f"⬇️سریال {hash} ({fa.replace('#', '').replace('_', ' ') } ) ، بازیرنویس چسبیده \n✅ قسمت : {E}\n💢[کل قسمت ها]({liink})\n\n⬇️1080👉\n⬇️720👉\n⬇️480👉\n⬇️240👉\n\n🆔👉 @dlmacvin_new"

        mkv240 = []
        mp4240 = []
        mkv480 = []
        mp4480 = []
        mkv720 = []
        mp4720 = []
        mkv1080 = []
        mp41080 = []
        F1 = None
        F2 = None
        F3 = None
        F4 = None
        # Duble Haaye 3 Ya 4 Filee
        if (message.chat.id == -1001457054266) and ((X in NoCopy) or (X in Copy)):
            kanal = -1001352276966

            
            # Zirnevis haaye 6 Ya 8 Filee
            if message.text:

                M240 = f"( {m} ) بازیرنویس چسبیده\n👌قسمت : {y}\n🔹کیفیت : 240"

                M480 = f"( {m} ) بازیرنویس چسبیده\n👌قسمت : {y}\n🔹کیفیت : 480"

                M720 = f"( {m} ) بازیرنویس چسبیده\n👌قسمت : {y}\n🔹کیفیت : 720"

                M1080 = f"( {m} ) بازیرنویس چسبیده\n👌قسمت : {y}\n🔹کیفیت : 1080"

                async for mkv240p in User.search_messages(chat_id=message.chat.id, query=M240, filter='document'):
                    Fnme = mkv240p.document.file_name
                    mkv240.append(Fnme)

                async for mp4240p in User.search_messages(chat_id=message.chat.id, query=M240, filter='video'):
                    Fnme = mp4240p.video.file_name
                    mp4240.append(Fnme)

                async for mkv480p in User.search_messages(chat_id=message.chat.id, query=M480, filter='document'):
                    Fnme = mkv480p.document.file_name
                    mkv480.append(Fnme)

                async for mp4480p in User.search_messages(chat_id=message.chat.id, query=M480, filter='video'):
                    Fnme = mp4480p.video.file_name
                    mp4480.append(Fnme)

                async for mkv720p in User.search_messages(chat_id=message.chat.id, query=M720, filter='document'):
                    Fnme = mkv720p.document.file_name
                    mkv720.append(Fnme)

                async for mp4720p in User.search_messages(chat_id=message.chat.id, query=M720, filter='video'):
                    Fnme = mp4720p.video.file_name
                    mp4720.append(Fnme)

                async for mkv1080p in User.search_messages(chat_id=message.chat.id, query=M1080, filter='document'):
                    Fnme = mkv1080p.document.file_name
                    mkv1080.append(Fnme)

                async for mp41080p in User.search_messages(chat_id=message.chat.id, query=M1080, filter='video'):
                    Fnme = mp41080p.video.file_name
                    mp41080.append(Fnme)

                if mp4240 and mp4480 and mp4720 and mkv240 and mkv720 and mkv480:
                    if mkv1080 and mp41080:
                        gold = "f"
                        if gold == "f":
                            await mp4240p.copy(chat_id=kanal)
                            await mp4480p.copy(chat_id=kanal)
                            await mp4720p.copy(chat_id=kanal)
                            await mp41080p.copy(chat_id=kanal)
                            F1 = await mkv240p.copy(chat_id=kanal)
                            F2 = await mkv480p.copy(chat_id=kanal)
                            F3 = await mkv720p.copy(chat_id=kanal)
                            F4 = await mkv1080p.copy(chat_id=kanal)
                        await bot.copy_message(chat_id=kanal, from_chat_id=-1001441684079, message_id=msgid, caption=f"{kap}", parse_mode='markdown')
                        await F1.copy(chat_id=kanal)
                        await F2.copy(chat_id=kanal)
                        await F3.copy(chat_id=kanal)
                        await F4.copy(chat_id=kanal)
                        await F1.delete()
                        await F2.delete()
                        await F3.delete()
                        await F4.delete()
                    elif (not mkv1080) and (not mp41080):
                        gold = "f"
                        if gold == "f":
                            await mp4240p.copy(chat_id=kanal)
                            await mp4480p.copy(chat_id=kanal)
                            await mp4720p.copy(chat_id=kanal)
                            F1 = await mkv240p.copy(chat_id=kanal)
                            F2 = await mkv480p.copy(chat_id=kanal)
                            F3 = await mkv720p.copy(chat_id=kanal)
                        await bot.copy_message(chat_id=kanal, from_chat_id=-1001441684079, message_id=msgid, caption=f"{kap}", parse_mode='markdown')
                        await F1.copy(chat_id=kanal)
                        await F2.copy(chat_id=kanal)
                        await F3.copy(chat_id=kanal)
                        await F1.delete()
                        await F2.delete()
                        await F3.delete()
                    if kap2 is not None:
                        await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=f"{kap2}", parse_mode='markdown')






Bot.start()
User.start()
# Loop Clients till Disconnects
idle()
# After Disconnects,
# Stop Clients
Bot.stop()
User.stop()
