from time import sleep

import telebot
from selenium import webdriver
from telebot import types

import Config


bot = telebot.TeleBot(Config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Запускаем Бота')

@bot.message_handler(commands=['button'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    print(markup)
    but_1 = types.InlineKeyboardButton('Будем искать видосы?',callback_data='find_vid_1')
    but_2 = types.InlineKeyboardButton('Нам не нужны видосы?',callback_data='find_vid_0')
    markup.add(but_1,but_2)

    bot.send_message(message.chat.id, 'Это был ВАШ выбор',reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'find_vid_1':
            research_video(call.message)
        else:
            ask_fignia(call.message)
            break



@bot.message_handler(commands=['vind_video'])
def research_video(message):
    msg = bot.send_message(message.chat.id,'Какое видео ВАМ нужно?')
    bot.register_next_step_handler(msg,search)

@bot.message_handler(commands=['text'])
def ask_fignia(message):
    bot.send_message(message.chat.id,'Я не ебу что ты от меня хочешь')
def search(message):
    driver = webdriver.Chrome()
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