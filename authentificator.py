def login(bot, message, db):
    # получаем id пользователя
    user_id = message.from_user.id
    # делаем запрос в базу данных о том есть ли данный пользователь
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()
    if result:
        bot.send_message(message.chat.id, 'Ты уже зарегистрированы')
    else:
        bot.send_message(message.chat.id, 'Регистрация в бота')
    bot.send_message(message.chat.id, user_id)

def register(bot, message):
    bot.send_message(message.chat.id, 'Регистрация в бота')