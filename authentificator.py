import mysql.connector
from mysql.connector import errorcode
from telebot import types
import datetime
import bcrypt

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
        bot.register_next_step_handler(login, lambda message: self.get_login(bot, message))

    def get_login(self, bot, message):
        # код авторизации
        login = message.text
        print(login)
        self.cursor.execute("SELECT * FROM users WHERE login = %s", (login,))
        result = self.cursor.fetchone()
        if result is None:
            bot.send_message(message.chat.id, "Такого пользователя не существует!")
            log_mark = types.InlineKeyboardMarkup(row_width=2)
            register = types.InlineKeyboardButton(text='Зарегистрироваться', callback_data='register')
            no_reg = types.InlineKeyboardButton(text='Отмена', callback_data='no_register')
            log_mark.add(register, no_reg)
            bot.send_message(message.chat.id, "Хотите зарегистрироваться?", reply_markup=log_mark)
        else:
            bot.send_message(message.chat.id, "Введите пароль!")

    def register(self, bot, message):
        # код регистрации
        bot.send_message(message.chat.id, "Начало регистрации!")
        # запрашиваем логин пользователя
        login = bot.send_message(message.chat.id, "Введите логин!")
        bot.register_next_step_handler(login, lambda message: self.reg_user(bot, message))

    def reg_user(self, bot, message):
        # запрашиваем пароль пользователя
        self.login = message.text
        print(self.login)
        password = bot.send_message(message.chat.id, "Введите пароль!")
        bot.register_next_step_handler(password, lambda message: self.reg_pass(bot, message))

    def reg_pass(self, bot, message):
        # шифруем пароля пользователя
        password = message.text
        print(password)
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.save_user(bot, message)

    def no_register(self, bot, message):
        # код отмены регистрации
        bot.send_message(message.chat.id, "Отмена! Пока!")

    def save_user(self, bot, message):
        # сохранение пользователя в базе данных
        print(self.login)
        print(self.hashed_password)       
        query = "INSERT INTO users (login, password) VALUES (%s, %s)"
        values = (self.login, self.hashed_password)
        self.cursor.execute(query, values)

        self.db.commit()