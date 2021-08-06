import random
import Config
import telebot
from telebot.types import Message

bot = telebot.TeleBot(Config.TOKEN)

@bot.message_handler(content_types=['text'])
# def echo_rand_int(message: Message):
#     bot.reply_to(message,str(random.random()))
# bot.polling(timeout=10)

def repeat_all_messages(message):
    bot.reply_to(message, message.text)

bot.polling(timeout=10)