import random

import Config
import telebot
from time import sleep
from selenium import webdriver
from telebot.types import Message

driver = webdriver.Chrome()

bot = telebot.TeleBot(Config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Запускаем Бота')

@bot.message_handler(commands=['vind_video'])
def research_video(message):
    msg = bot.send_message(message.chat.id,'Какое видео ВАМ нужно?')
    bot.register_next_step_handler(msg,search)

@bot.message_handler(commands=['text'])
def ask_fignia(message):
    bot.send_message(message.chat.id,'Я не ебу что ты от меня хочешь')
def search(message):
    bot.send_message(message.chat.id,'Ща все будет')
    url_video = 'https://www.youtube.com/results?search_query=' + message.text + '&sp=EgIIAw%253D%253D'
    driver.get(url_video)
    sleep(1)
    vidosik = driver.find_elements_by_id('video-title')
    video = 0
    while video != 5:
        bot.send_message(message.chat.id,vidosik[video].get_attribute('href'))
        video += 1


bot.polling()
