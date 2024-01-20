from telebot import types
def send_welcome_message(bot, message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    login = types.InlineKeyboardButton(text='Войти', callback_data='login')
    register = types.InlineKeyboardButton(text='Зарегистрироваться', callback_data='register')
    markup.add(login, register)
    bot.send_message(message.chat.id, 'Привет! Я', reply_markup=markup)


def send_help_message(bot, message):
    bot.send_message(message.chat.id, 'Помощь')