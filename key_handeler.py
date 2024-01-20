from telebot import *

@bot.callback_query_handler(func=lambda call: True)
