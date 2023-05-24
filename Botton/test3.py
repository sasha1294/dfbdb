from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b2 = KeyboardButton('Game')
b3 = KeyboardButton('Media')
b4 = KeyboardButton('Songs')

kdd_test3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kdd_test3.add(b2).add(b3).add(b4)