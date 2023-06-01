from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
storage = MemoryStorage()
TOKEN = "6250035779:AAHPsPZsKDszPmRJDT21k-9RDbrvpvZ3ims"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)