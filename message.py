
from authentificator import *

class MessageHandler:
    @staticmethod
    def send_welcome_message(bot, message):
        markup = types.InlineKeyboardMarkup(row_width=2)
        login = types.InlineKeyboardButton(text='Войти', callback_data='login')
        register = types.InlineKeyboardButton(text='Зарегистрироваться', callback_data='register')
        markup.add(login, register)
        bot.send_message(message.chat.id, 'Привет! Это я бот BlackCourse!  \nТвой надежный помощник в мир новых и интересных знаний! \nС помощью нашего бота ты сможешь: \n•Получить те знания которые ты так хотел, но не мог ранее.\n•Получить все необходимые навыки.\n•Пройти весь путь от А до Я с нашим инновационным подходом.\n•Персонализированное обучение.\nШирокий выбор курсов для обучения.\n•Гибкость и доступность.\n•Мониторинг прогресса и достижений.\n•Система рекомендаций в соответствии с вашими успехами.\n•Удобный доступ.\n•Мгновенная обратная связь.\n•Система наград и мотиваций.\n•Интерактивное обучение.\n•Мультиязычность.\n•Бот доступен во всех странах!', reply_markup=markup)

    def send_help_message(self, bot, message):  # Исправить имя функции здесь
        bot.send_message(message.chat.id, 'Помощь')

    def no_register(self, bot, message):
        bot.send_message(message.chat.id, "Хорошо, до скорой встречи!")