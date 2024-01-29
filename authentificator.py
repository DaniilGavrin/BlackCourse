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
        # проверяем подключение к базе данных
        try:
            self.cursor.execute("SELECT * FROM users")
            self.db.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
    def login(self, bot, message):
        # код авторизации
        bot.send_message(message.chat.id, "Введите логин!")

        login = message.text
        print(login)
        self.cursor.execute("SELECT * FROM users WHERE login = %s", (login,))
        print(self.cursor.rowcount())

        if cursor.rowcount() > 0:
            msg = bot.send_message(message.chat.id, "Введите пароль!")
        elif cursor.rowcount() == 0:
            msg = bot.send_message(message.chat.id, "Пользователь с таким логином не существует!")
        else:
            msg = bot.send_message(message.chat.id, "Ошибка!")

    def register(self, bot, message):
        # код регистрации
        pass

    def save_user(self, bot, message):
        # код сохранения пользователя в базе данных
        pass