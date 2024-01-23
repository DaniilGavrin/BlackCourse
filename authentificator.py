def login(bot, message):
    bot.send_message(message.chat.id, "Авторизация в бота")

def register(bot, message):
    bot.send_message(message.chat.id, 'Регистрация в бота')