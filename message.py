def send_welcome_message(bot, message):
    bot.send_message(message.chat.id, 'Привет! Я')

def send_help_message(bot, message):
    bot.send_message(message.chat.id, 'Помощь')