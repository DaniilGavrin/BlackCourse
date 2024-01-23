# Импортируем telebot + requests
import telebot
from telebot import *
import requests
from message import *
from license import *
from authentificator import *
import mysql.connector

# подключение к базе данных
db = mysql.connector.connect(
    host="172.18.0.2",
    user="root",
    password="090807",
    database="bottg"
)
cursor = db.cursor()

# проверяем подключение к базе данных
try:
    cursor.execute("SELECT * FROM users")
    db.commit()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


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