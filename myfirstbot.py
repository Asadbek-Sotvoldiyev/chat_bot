import telebot
import wikipedia as wp
import requests

wp.set_lang('uz')
def wiki_wiki(text):
    return wp.summary(text, sentences=20)
bot = telebot.TeleBot("6997348052:AAFwONyYLho-VIUd_t9qU8mRSkdrgIYe-gg")

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    bot.send_message(message.chat.id, f'Salom {name}! Qanday ma\'lumot kerak bo\'lsa so\'rashingiz mumkin?')

@bot.message_handler(func=lambda message: True)
def send(message):
    text = message.text

    if text == 'Sen kimsan' or text == 'Kimsan' or text == 'kimsan' or text == 'sen kimsan':
        bot.send_message(message.chat.id, "Men AI ga asoslangan botman. Iltimos qiziqtirgan savollaringiz bo'lsa menga yuboring. Qo'limdan kelgancha yordam beraman...")
    elif text == "obhavo" or text == 'Obhavo' or text == 'ob-havo' or text == "Ob-havo" or 'obhavo' in text or 'ob-havo' in text:
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Tashkent,UZ&units=metric&appid=a9d86a9dc54f8caf39ac424735ffc2e6')
        text = f"Lokatsiya: {r.json()['name']}\nDavlat: {r.json()['sys']['country']}\nHavo harorati: {r.json()['main']['temp']} C\nNamlik: {r.json()['main']['humidity']}%\nShamol tezligi: {r.json()['wind']['speed']}m/s"
        bot.send_message(message.chat.id, text)
    else:
        try:
            bot.send_message(message.chat.id, "Tayyorlayabman! Iltimos biroz kuting....")
            bot.send_message(message.chat.id, wiki_wiki(text))

        except:
            bot.send_message(message.chat.id, "Kechirasiz! Sizni tushuna olmadim iltimos aniqroq yozing!")


bot.polling(none_stop=True)
