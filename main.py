# Импортируем telebot + requests
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import requests
from message import *
from license import *
from authentificator import *
import mysql.connector
from mysql.connector import errorcode

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6786465313:AAGWvU4ppWSAmP37BKEXVfW63hKWqycjzQk")

dp = Dispatcher(bot, storage=MemoryStorage())

class Bot:
    def __init__(self):
        self.dp = dp
    
    async def start(self, message: types.Message):
        MessageHandler.send_welcome_message(self, message: types.Message)