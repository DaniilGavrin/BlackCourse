import mysql.connector
from mysql.connector import errorcode
from telebot import types
import datetime

class Authentificator:
    def __init__(self):
        db = mysql.connector.connect(
            host="172.17.0.2",
            user="root",
            password="090807",
            database="bottg"
        )
        cursor = db.cursor()
    def login(self, bot, message):
        # код авторизации
        bot.send_message(message.chat.id, "Введите логин!")
        cursor = self.db.cursor()

        login = message.text

        cursor.execute("SELECT * FROM users WHERE login = %s", (login,))
        print(cursor.rowcount())

        if cursor.rowcount() > 0:
            msg = bot.send_message(message.chat.id, "Введите пароль!")

    def register(self, bot, message):
        # код регистрации
        pass

    def save_user(self, bot, message):
        # код сохранения пользователя в базе данных
        pass