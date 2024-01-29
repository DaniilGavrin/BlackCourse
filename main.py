# Импортируем telebot + requests
import telebot
from telebot import *
import requests
from message import *
from license import *
from authentificator import *
import mysql.connector
from mysql.connector import errorcode

class Bot:
    def __init__(self):
        # подключение к базе данных
        db = mysql.connector.connect(
            host="172.17.0.2",
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

        # Инициализация бота
        self.bot = telebot.TeleBot("6786465313:AAGWvU4ppWSAmP37BKEXVfW63hKWqycjzQk")

        # Регистрация обработчиков сообщений
        self.register_handlers()

    def run(self):
        # запуск бота
        self.bot.polling()

    def register_handlers(self):
        message_handler = MessageHandler()
        license_handler = LicenseHandler()
        authentificator = Authentificator()  # Добавить инициализацию объекта authentificator

        @self.bot.message_handler(commands=['start'])
        def start_message(message):
            message_handler.send_welcome_message(self.bot, message)

        @self.bot.message_handler(commands=['help'])
        def help_message(message):
            message_handler.send_help_message(self.bot, message)

        @self.bot.message_handler(commands=['license'])
        def give_license(message):
            license_handler.license(self.bot, message)

        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_query(call):
            try:
                if call.data == "login":
                    authentificator.login(self.bot, call.message)
                elif call.data == "register":
                    authentificator.register(self.bot, call.message)
                elif call.data == "no_register":
                    authentificator.no_register(self.bot, call.message)
                elif call.data == "license":
                    license_handler.license(self.bot, call)
                elif call.data == "message":
                    message_handler.message(self.bot, call)
            except Exception as e:
                print(e)
            

# Создаем экземпляр класса Bot
bot = Bot()

# Запуск бота
bot.run()