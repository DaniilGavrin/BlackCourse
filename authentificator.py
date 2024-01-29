import mysql.connector
from mysql.connector import errorcode
from telebot import types
import datetime

class Authentificator:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="172.17.0.2",
            user="root",
            password="090807",
            database="bottg"
        )
        self.cursor = self.db.cursor()
    def login(self, bot, message):
        # код авторизации
        login = bot.send_message(message.chat.id, "Введите логин!")
        bot.register_next_step_handler(login, self.get_login)

    def get_login(self, bot, message):
        # код авторизации
        login = message.text
        print(login)
        self.cursor.execute("SELECT * FROM users WHERE login = %s", (login,))
        result = self.cursor.fetchone()
        if result is None:
            bot.send_message(message.chat.id, "Такого пользователя не существует!")
        else:
            bot.send_message(message.chat.id, "Введите пароль!")
            bot.register_next_step_handler(message, self.get_password)

    def register(self, bot, message):
        # код регистрации
        pass

    def save_user(self, bot, message):
        # код сохранения пользователя в базе данных
        pass