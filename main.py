# Импортируем telebot + requests
import telebot
import requests
from message import *

# НАчальный код для работы с ботом
bot = telebot.TeleBot("6786465313:AAGWvU4ppWSAmP37BKEXVfW63hKWqycjzQk")

@bot.message_handler(commands=['start'])
def start_message(message):
    send_welcome_message(bot, message)
    
bot.polling()