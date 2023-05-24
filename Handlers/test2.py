from bot_create import dp
from Botton.test3 import kdd_test3
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from database import test1
from Handlers import test6


class FSMuser(StatesGroup):
    download_state = State()
    game_name = State()
    name_media = State()
    name_songs = State()


async def start(message: types.Message):
    await message.answer(f"Здравствуйте, это бот для скачивания медиа файлов, игр и музыки. Приятного пользования!")
    await message.answer(f'Выберите тип данных', reply_markup=kdd_test3)
    await FSMuser.download_state.set()


async def download_type(message: types.Message):
    if message.text == 'Game':
        await message.answer(f'Перешёл в игры')
        await message.answer('Впишите название игры')
        await FSMuser.game_name.set()
    if message.text == 'Media':
        await message.answer(f'Перешёл в медиа')
        await message.answer('Впишите название media')
        await FSMuser.name_media.set()
    if message.text == 'Songs':
        await message.answer(f'Перешёл в песни')
        await message.answer('Впишите название песни')
        await FSMuser.name_songs.set()


async def choose_game(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['game_name'] = message.text
        await test1.sql_add_command_for_games(message.text)
    await message.answer("Жди - выполняется запрос!")
    await message.answer(await test6.result())
    await test1.delete()
    await message.answer("Перезапустите бота")
    await state.finish()


async def choose_media(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_media'] = message.text
        await test1.sql_add_command_for_media(message.text)
    await message.answer("Жди - выполняется запрос!")
    await message.answer(await test6.result2())
    await test1.delete()
    await message.answer('Перезапустите бота')
    await state.finish()


async def choose_songs(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_songs'] = message.text
        await test1.sql_add_command_for_songs(message.text)
    await message.answer("Жди - выполняется запрос!")
    await message.answer(await test6.result3())
    await test1.delete()
    await message.answer("Перезапустите бота")
    await state.finish()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_message_handler(download_type, content_types=['text'], state=FSMuser.download_state)
    dp.register_message_handler(choose_game, state=FSMuser.game_name)
    dp.register_message_handler(choose_media, state=FSMuser.name_media)
    dp.register_message_handler(choose_songs, state=FSMuser.name_songs)
