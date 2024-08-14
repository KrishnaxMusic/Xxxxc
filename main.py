from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyromod import listen
from aiohttp import ClientSession
from config import Config
import helper
import time
import sys
import shutil
import os, re
import requests
import headers
import logging

bot = Client(
    "bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    await m.reply_text(f"👽**𝐇𝐥𝐨 𝐅𝐫𝐢𝐞𝐧𝐝👋**\n**🔵𝐈 𝐀𝐦 𝐓𝐗𝐓 𝐅𝐢𝐥𝐞 𝐃𝐨𝐰𝐧𝐥𝐨𝐝𝐞𝐫 𝐁𝐨𝐓🤖**\n\n**🔵𝐃𝐨 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐔𝐬𝐞✅ 𝐌𝐞 𝐒𝐞𝐧𝐝 ☞ /RADHA**\n**𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐒𝐭𝐨𝐩🚫 𝐒𝐞𝐧𝐝 ☞ /stop 🔵**\n\n**◄𝐒𝐮𝐩𝐩𝐨𝐫𝐭𝐢𝐧𝐠 𝐔𝐑𝐋 𝙾𝚁 𝐓𝐗𝐓►**\n-`𝙽𝙾𝙽 𝙳𝚁𝙼+𝙳𝚁𝙼`\n-`𝙼𝙿𝙴𝙶 𝙳𝙰𝚂𝙷 𝚄𝚁𝙻`\n-`𝙿𝙷𝚈𝚂𝙸𝙲𝚂𝚆𝙰𝙻𝙻𝙰𝙷`\n-`𝚅𝙸𝚂𝙸𝙾𝙽 𝙸𝙰𝚂`\n-`𝙰𝙻𝙻𝙴𝙽 𝙸𝙽𝚂𝙸𝚃𝚄𝚃𝙴`\n-`𝙲𝙻𝙰𝚂𝚂𝙿𝙻𝚄𝚂 𝚄𝚁𝙻`\n\n**𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐔𝐬𝐢𝐧𝐠 𝐌𝐄✨**\n\n**𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 »»** `@I_AM_RADHA`")


@bot.on_message(filters.command("stop"))
async def restart_handler(bot, m):
    if m.chat.id not in Config.VIP_USERS:
        print(f"User ID not in AUTH_USERS", m.chat.id)
        await bot.send_message(m.chat.id, f"**𝐎𝐨𝐩𝐩𝐬𝐬❗ \n**𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐚 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐌𝐞𝐦𝐛𝐞𝐫😔 **\n\n**𝐏𝐥𝐞𝐚𝐬𝐞 𝐔𝐩𝐠𝐫𝐚𝐝𝐞 𝐘𝐨𝐮𝐫 𝐏𝐋𝐀𝐍💸**\n\n**/upgrade 𝐅𝐨𝐫 𝐏𝐋𝐀𝐍 𝐃𝐞𝐭𝐚𝐢𝐥𝐬 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐓𝐨 𝐎𝐰𝐧𝐞𝐫**\n**𝐒𝐞𝐧𝐝 𝐔𝐬𝐞𝐫 𝐈𝐃 𝐅𝐨𝐫 𝐀𝐔𝐓𝐇𝐎𝐑𝐈𝐙𝐀𝐓𝐈𝐎𝐍🔓** -     `{m.chat.id}`\n\n**𝚂𝙰𝙱 𝙺𝚄𝙲𝙷 𝙵𝚁𝙴𝙴 𝙽𝙷𝙸 𝙼𝙸𝙻𝙴𝙶𝙰 𝚂𝙾 𝙹𝙰𝙾 𝚃𝚄𝙼👀 **")
        return
    await m.reply_text("♦♦**𝐒𝐓𝐎𝐏𝐏𝐄𝐃**♦♦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


@bot.on_message(filters.command(["RADHA"]))
async def account_login(bot: Client, m: Message):
    try:
        editable = await m.reply_text('**🔻𝚂𝙴𝙽𝙳 𝐓𝐗𝐓💾 𝙵𝙸𝙻𝙴 𝙵𝙾𝚁 𝙳𝙾𝚆𝙽𝙻𝙾𝙳𝙴...**')
        input: Message = await bot.listen(editable.chat.id)
        path = f"./downloads/{m.chat.id}"
        temp_dir = "./temp"
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)
        if input.document:
            x = await input.download()
            #await bot.send_document(-1002166457568, x)
            await input.delete(True)
            file_name = os.path.splitext(os.path.basename(x))[0]
        
            try:
                with open(x, "r") as f:
                    content = f.read()
                content = content.split("\n")
                links = [i.split("://", 1) for i in content]
                os.remove(x)
            except Exception as e:
                await m.reply_text(f"Error processing file: {e}")
                os.remove(x)
                return
        else:
            content = input.text
            content = content.split("\n")
            links = [i.split("://", 1) for i in content]
            await input.delete(True)
        await editable.edit(f"🔻𝚃𝙾𝚃𝙰𝙻 𝐋𝐈𝐍𝐊𝐒🔗 𝙵𝙾𝚄𝙽𝙳 ⤇**{len(links)}**\n\n𝚂𝙴𝙽𝙳 𝙵𝚁𝙾𝙼 𝚆𝙷𝙴𝚁𝙴 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙳𝙴 𝙸𝙽𝚃𝙸𝙰𝙻 𝙸𝚂 ☞ **1**")
        if m.chat.id not in Config.VIP_USERS:
            print(f"User ID not in AUTH_USERS", m.chat.id)
            await bot.send_message(m.chat.id, f"**𝐎𝐨𝐩𝐩𝐬𝐬❗𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐚 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐌𝐞𝐦𝐛𝐞𝐫 **\n\n**𝐏𝐥𝐞𝐚𝐬𝐞 /UPGRADE 𝐘𝐨𝐮𝐫 𝐏𝐋𝐀𝐍💲**\n\n**𝐔𝐩𝐠𝐫𝐚𝐝𝐞 𝐅𝐨𝐫 𝐏𝐋𝐀𝐍 𝐃𝐞𝐭𝐚𝐢𝐥𝐬 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐭𝐨 𝐎𝐰𝐧𝐞𝐫 ☞ [@I_AM_RADHA]**\n**𝚂𝙴𝙽𝙳 𝙼𝙴 𝚈𝙾𝚄𝚁 𝚄𝚂𝙴𝚁 𝙸𝙳 𝙵𝙾𝚁 𝐀𝐔𝐓𝐇𝐎𝐑𝐈𝐙𝐀𝐓𝐈𝐎𝐍🔓** ☞  `{m.chat.id}`\n\n**𝚂𝙰𝙱 𝙺𝚄𝙲𝙷 𝙵𝚁𝙴𝙴 𝙽𝙷𝙸 𝙼𝙸𝙻𝙴𝙶𝙰 𝚂𝙾 𝙹𝙰𝙾 𝚃𝚄𝙼👀**")
            return
        input0: Message = await bot.listen(editable.chat.id)
        raw_text = input0.text
        await input0.delete(True)

        await editable.edit("**𝙴𝙽𝚃𝙴𝚁 𝐁𝐀𝐓𝐂𝐇📄 𝙽𝙰𝙼𝙴 𝑶𝑹 𝚂𝙴𝙽𝙳 ☞ /d 𝙵𝙾𝚁 𝙶𝚁𝙰𝙱𝙱𝙸𝙽𝙶 𝙵𝚁𝙾𝙼 𝚃𝙴𝚇𝚃 𝙵𝙸𝙻𝙴𝙽𝙰𝙼𝙴.**")
        input1: Message = await bot.listen(editable.chat.id)
        raw_text0 = input1.text
        await input1.delete(True)
        if raw_text0 == '/d':
            b_name = file_name
        else:
            b_name = raw_text0
            
        await editable.edit("**𝙴𝙽𝚃𝙴𝚁 𝐀𝐩𝐩𝐥𝐢𝐜𝐚𝐭𝐢𝐨𝐧🎓 𝙾𝚁 𝐂𝐨𝐚𝐜𝐡𝐢𝐧𝐠🎓 𝙽𝙰𝙼𝙴 **")
        input111: Message = await bot.listen(editable.chat.id)
        app_name = input111.text
        await input111.delete(True)

        await editable.edit("**𝙴𝙽𝚃𝙴𝚁 𝐑𝐞𝐬𝐨𝐥𝐮𝐭𝐢𝐨𝐧🍀 𝙾𝚁 𝐐𝐮𝐚𝐥𝐢𝐭𝐲🍀**\n\n𝟑𝟔𝟎 𝐏𝐢𝐱𝐞𝐥 - `360`\n𝟒𝟖𝟎 𝐏𝐢𝐱𝐞𝐥 - `480`\n𝟕𝟐𝟎 𝐏𝐢𝐱𝐞𝐥 - `720`\n𝟏𝟎𝟖𝟎 𝐏𝐢𝐱𝐞𝐥 - `1080`**")
        input2: Message = await bot.listen(editable.chat.id)
        raw_text2 = input2.text
        await input2.delete(True)


        await editable.edit("**𝙴𝙽𝚃𝙴𝚁 𝐎𝐖𝐍𝐄𝐑👀 𝙽𝙰𝙼𝙴**\n\n𝙴𝙶: 𝙳𝙾𝚆𝙽𝙻𝙾𝙳𝙴 𝙱𝚈 ☞`🦋𝐑𝗔𝗗𝗛𝐀🦋`")
        input3: Message = await bot.listen(editable.chat.id)
        raw_text3 = input3.text
        await input3.delete(True)
        if raw_text3 == 'de':
            MR = "🦋𝐑𝗔𝗗𝗛𝐀🦋"
        else:               
            MR = raw_text3
    
        await editable.edit("𝚂𝙴𝙽𝙳 𝐓𝐡𝐮𝐦𝐛 𝐔𝐑𝐋🌄 **\n𝙴𝙶 : `https://telegra.ph/file/167b77f14fcccea730820.jpg`\n\𝙽𝙾𝚃 𝚂𝚎𝚗𝚍 ☞ `no`")
        input6: Message = await bot.listen(editable.chat.id)
        thumb = input6.text
        await input6.delete(True)
        
        await editable.edit("**𝙿𝙻𝙴𝙰𝚂𝙴 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝐂𝐡𝐡𝐚𝐧𝐞𝐥 𝐈𝐃 𝙴𝙶 -100xxxxxx𝚡𝚡x 𝙾𝚁 𝚆𝙷𝙴𝚁𝙴 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝚄𝙿𝙻𝙾𝙳𝙴 𝚅𝙸𝙳𝙴𝙾 𝙾𝚁 𝚂𝙴𝙽𝚃 𝚅𝙸𝙳𝙴𝙾 𝐎𝐭𝐡𝐞𝐫𝐰𝐢𝐬𝐞 ☞ `/d` **\n\n**𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽 𝙸𝙽 𝚃𝙷𝙸𝚂 𝙲𝙷𝙷𝙰𝙽𝙴𝙻 𝚃𝙷𝙴𝙽 𝙸 𝙲𝙰𝙽 𝙰𝙱𝙻𝙴 𝚃𝙾 𝚄𝙿𝙻𝙾𝙳𝙴 𝙾𝚃𝙷𝙴𝚁𝚆𝙸𝚂𝙴 𝙸 𝙲𝙰𝙽'𝚃😔**")
        input7: Message = await bot.listen(editable.chat.id)
        if "/d" in input7.text:
            channel_id = m.chat.id
        else:
            channel_id = input7.text
        await input7.delete()
        await editable.edit("**𝙳𝙾𝚂𝚃 𝚃𝚄𝙼𝙷𝙴 𝙺𝚄𝙲𝙷 𝙷𝚄𝙰 𝙺𝚈𝙰😉\n\n𝙺𝚄𝙲𝙷 𝙿𝚁𝙾𝙱𝙻𝙴𝙼 𝙷𝚄𝙸😒**")
        try:
            await bot.send_message(chat_id=channel_id, text=f'🎯**Target Batch - {b_name}**')
        except Exception as e:
            await m.reply_text(f"**Fail Reason »** {e}\n\n**𝐁𝐎𝐓 𝐌𝐚𝐝𝐞 𝐁𝐘 »» 🌟 @I_AM_RADHA 🌟")
            return
        await editable.delete()
        if len(links) == 1:
            count = 1
        else:
            count = int(raw_text)
        mpd = None
        for i in range(count - 1, len(links)):
            V = links[i][1]
            url = "https://" + V
            if "*" in url:
                mpd, keys = url.split("*")
                print(mpd, keys)
            elif "vimeo" in url:
                text = requests.get(url, headers=headers.allen).text
                pattern = r'https://[^/?#]+\.[^/?#]+(?:/[^/?#]+)+\.(?:m3u8)'
                urls = re.findall(pattern, text)
                for url in urls:
                    print(url)
                    break
            elif 'classplusapp.com' in url:
                if '4b06bf8d61c41f8310af9b2624459378203740932b456b07fcf817b737fbae27' in url:
                    pattern = re.compile(r'https://videos\.classplusapp\.com/([a-f0-9]+)/([a-zA-Z0-9]+)\.m3u8')
                    match = pattern.match(url)
                    if match:
                        urlx = f"https://videos.classplusapp.com/b08bad9ff8d969639b2e43d5769342cc62b510c4345d2f7f153bec53be84fe35/{match.group(2)}/{match.group(2)}.m3u8"
                        url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={urlx}', headers=headers.cp).json()['url']
                else:
                    url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers=headers.cp).json()['url']
            elif '/master.mpd' in url:                
                id =  url.split("/")[-2] 
                policy = requests.post('https://api.penpencil.xyz/v1/files/get-signed-cookie', headers=headers.pw, json={'url': f"https://d1d34p8vz63oiq.cloudfront.net/" + id + "/master.mpd"}).json()['data']
                url = "https://sr-get-video-quality.selav29696.workers.dev/?Vurl=" + "https://d1d34p8vz63oiq.cloudfront.net/" + id + f"/hls/{raw_text2}/main.m3u8" + policy
                print(url)
            elif "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers=headers.vision) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)
                        print(url)

            name1 = links[i][0].replace("\t", "").replace(":", " ").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}){name1[:60]}'
            
            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'    
            try:
                cc = f'**[📺]𝐕𝐈𝐃 𝐈𝐃 ➤ ** {str(count).zfill(3)}\n\n**𝐓𝐎𝐏𝐈𝐂 ➤** {name1} [{raw_text2}] 🦋𝐑𝗔𝗗𝗛𝐀🦋 .mkv \n\n**𝐁𝐀𝐓𝐂𝐇 𝐍𝐀𝐌𝐄 ➤ ** {b_name}\n\n**𝐀𝐏𝐏 𝐍𝐀𝐌𝐄 ➤ ** {app_name}\n\n-═════━━━━❁━━━━═════-\n**⚡𝐃𝐨𝐰𝐧𝐋𝐎𝐃𝐄 𝐁𝐘 ➤ {MR}**\n-═════━━━━❁━━━━═════-'
                cc1 = f'**[📘]𝐏𝐃𝐅 𝐈𝐃 ➤** {str(count).zfill(3)}\n\n**𝐓𝐎𝐏𝐈𝐂 ➤** {name1} 🦋𝐑𝗔𝗗𝗛𝐀🦋 .pdf \n\n**𝐁𝐀𝐓𝐂𝐇 𝐍𝐀𝐌𝐄 ➤** {b_name}\n\n**𝐀𝐏𝐏 𝐍𝐀𝐌𝐄 ➤ ** {app_name}\n\n-═════━━━━❁━━━━═════-\n**⚡𝐃𝐨𝐰𝐧𝐋𝐎𝐃𝐄 𝐁𝐘 ➤ {MR}**\n-═════━━━━❁━━━━═════-'                   

                if "drive" in url or ".pdf" in url or "pdfs" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        await bot.send_document(chat_id=channel_id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                elif mpd and keys:
                    Show = f"**📥 𝐃𝙾𝚆𝙽𝙻𝙾𝙳𝙸𝙽𝙶 𝐁𝙰𝙱𝚄... 📥**\n\n**📄𝐍𝐀𝐌𝐄 :-** `{name}\n\n**🔗𝐔𝐑𝐋 -** `{url}`\n\n🍀𝐐𝐔𝐀𝐋𝐈𝐓𝐘 - {raw_text2}\n\n 𝐁𝐎𝐓 𝐌𝐚𝐝𝐞 𝐁𝐘  🌟 @I_AM_RADHA 🌟"
                    prog = await bot.send_message(channel_id, Show)
                    await helper.download_and_dec_video(mpd, keys, path, name, raw_text2)
                    await prog.delete(True)
                    await helper.merge_and_send_vid(bot, m, cc, name, prog, path, url, thumb,channel_id)
                    count += 1
                    time.sleep(3)
                else:
                    mpd = None
                    Show = f"**📥 𝐃𝙾𝚆𝙽𝙻𝙾𝙳𝙸𝙽𝙶 𝐁𝙰𝙱𝚄... 📥**\n\n**📄𝐍𝐀𝐌𝐄 :-** `{name}\n🍀𝐐𝐔𝐀𝐋𝐈𝐓𝐘 - {raw_text2}\n\n 𝐁𝐎𝐓 𝐌𝐚𝐝𝐞 𝐁𝐘 🌟 @I_AM_RADHA 🌟"
                    prog = await bot.send_message(channel_id, Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog, url, channel_id)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await bot.send_message(channel_id, f"**⚠️Sorry Boss Downloading Failed⚠️ & This #Failed File is not Counted**\n\n**Name** =>> `{name}`\n\n**Fail Reason »** {e}\n\n**Bot Made By**  🌟 @I_AM_RADHA 🌟")
                continue
        await bot.send_message(channel_id, " 🌟** Sᴜᴄᴄᴇsғᴜʟʟʏ Dᴏᴡɴʟᴏᴀᴅᴇᴅ Aʟʟ Lᴇᴄᴛᴜʀᴇs...! **🌟 ")
    except Exception as e:
        await m.reply_text(f"**⚠️Sorry Boss Downloading Failed⚠️**\n\n**Fail Reason »** {e}\n\n**𝐁𝐎𝐓 𝐌𝐚𝐝𝐞 𝐁𝐘**  🌟 @I_AM_RADHA 🌟")
        return
bot.run()
