import requests as r
import random
import telebot

bot = telebot.TeleBot("6231042647:AAH7llVSqz_haI3dszLuKRtDb28vSeFOi7g")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Введи команду /ip, чтобы рандомизировать IP-адресс")
@bot.message_handler(commands=['ip'])
    def ip(message):
        bot.send_message(message.chat.id, "Вот, что:")
        ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}:{random.randint(80, 10000)}"
        url = r.get("https://google.com", proxies={"http": ip, "https:": ip}, timeout=1.5)
        if url == 200:
            bot.send_message(message.chat.id, ip)
        else:
            bot.send_message(message.chat.id, f"Прокси {ip} не работает!")
bot.polling(none_stop=True)
