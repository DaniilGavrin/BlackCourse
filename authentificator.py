import mysql.connector
from mysql.connector import errorcode
from telebot import types
import datetime

def login(bot, message):
    # подключение к базе данных
    bot.send_message(message.chat.id, "Авторизация в бота")
    # получаем user_id пользователя
    user_id = message.from_user.id
    print(user_id)
    db = mysql.connector.connect(
    host="172.17.0.2",
    user="root",
    password="090807",
    database="bottg"
    )
    cursor = db.cursor()
    # делаем запрос в базу данных users и проверяем есть ли такой пользователь в базе данных
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    print(cursor.rowcount)
    # если такого пользователя нету в базе данных то пишем об этом сообщение
    if cursor.rowcount == 0:
        bot.send_message(message.chat.id, "Пользователь не зарегистрирован")
        #спрашиваем хочет ли он зарегистрироваться
        mark = types.InlineKeyboardMarkup(row_width=2)
        yesregister = types.InlineKeyboardButton(text='Да', callback_data='regbot')
        noregister = types.InlineKeyboardButton(text='Не хочу', callback_data='noregister')
        mark.add(yesregister, noregister)
        bot.send_message(message.chat.id, "Зарегистрироваться?", reply_markup=mark)
    # если такого пользователя есть в базе данных то пишем об этом сообщение
    else:
        bot.send_message(message.chat.id, "Пользователь зарегистрирован")

def register(bot, message):
    bot.send_message(message.chat.id, 'Регистрация в бота')
    db = mysql.connector.connect(
    host="172.17.0.2",
    user="root",
    password="090807",
    database="bottg"
    )
    user_id = message.from_user.id
    print(user_id)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    # если такого пользователя нету в базе данных то пишем об этом сообщение
    if cursor.rowcount == 0:
        bot.send_message(message.chat.id, "Начало регистрации в бота")
        # спрашиваем пользователя его username и пишем в переменную
        msg = bot.send_message(message.chat.id, "Введите имя пользователя:")
        bot.register_next_step_handler(msg, save_username)
    else:
        bot.send_message(message.chat.id, "Вы всё-таки зарегистрированы")

def save_username(message):
    print("хуй")
    user_id = message.from_user.id
    print(user_id)
    username = message.text
    registration_date = datetime.datetime.now()
    print(registration_date)
    db = mysql.connector.connect(
    host="172.17.0.2",
    user="root",
    password="090807",
    database="bottg"
    )
    cursor = db.cursor()
    # Вставка в базу данных
    sql = "INSERT INTO users (user_id, username, registration_date) VALUES (%s, %s, %s)"
    val = (user_id, username, registration_date)
    cursor.execute(sql, val)
    db.commit()