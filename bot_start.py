from aiogram.utils import executor
from bot_create import dp
from database import test1

test1.db_start()
test1.delete_for_start()
print("бот вышел в онлайн")


from Handlers import test2

test2.register_handlers(dp)

executor.start_polling(dp, skip_updates=True)
