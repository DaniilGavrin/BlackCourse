# Импортируем telebot + requests
import telebot
import requests
from message import *
from authentificator import *
import MySQLdb

# подключение к базе данных
db = MySQLdb.connect(host="rc1d-vt509yuxvc4gn6hf.mdb.yandexcloud.net",
      port=3306,
      db="tgbot",
      user="bot_user",
      passwd="090807Dan4ik")
cursor = db.cursor()


# НАчальный код для работы с ботом
bot = telebot.TeleBot("6786465313:AAGWvU4ppWSAmP37BKEXVfW63hKWqycjzQk")

@bot.message_handler(commands=['start'])
def start_message(message):
    send_welcome_message(bot, message)

@bot.message_handler(commands=['help'])
def help_message(message):
    send_help_message(bot, message)


@bot.message_handler(commands=['login'])
def login(message):
    login(bot, message)
    
bot.polling()