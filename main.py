# Импортируем telebot + requests
import telebot
from telebot import *
import requests
from message import *
from license import *
from authentificator import *
import MySQLdb

# подключение к базе данных
db = MySQLdb.connect(host="172.18.0.2", user="root", passwd="090807", db="bottg")
cursor = db.cursor()

#проверяем подключение к базе данных\
try:
    cursor.execute("SELECT * FROM users")
    db.commit()
except:
    pass

# НАчальный код для работы с ботом
bot = telebot.TeleBot("6786465313:AAGWvU4ppWSAmP37BKEXVfW63hKWqycjzQk")

# Стартовое сообщение
@bot.message_handler(commands=['start'])
def start_message(message):
    send_welcome_message(bot, message)

# Сообщение со списком команд
@bot.message_handler(commands=['help'])
def help_message(message):
    send_help_message(bot, message)

# Лицензия
@bot.message_handler(commands=['license'])
def give_license(message):
    license(bot, message)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        if call.data == 'login':
            login(bot, call.message)
        elif call.data =='register':
            register(bot, call.message)
    except:
        pass

bot.polling()