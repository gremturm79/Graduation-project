from anecAPI import anecAPI
from aiogram import Dispatcher, Bot, executor, types
import logging
import time

TOKEN = '5466575537:AAFECFVNJo1KqgKXbXPDPiui2Np1FoNF5XY'
MSG = 'Как дела, {}?'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler()
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f'Привет, {message.from_user.full_name}, анектоды для Вас')
    lst = [anecAPI.modern_joke(),'\n\N{fire}', anecAPI.soviet_joke(),'\n\N{fire}', anecAPI.random_joke()]

    await message.reply(f'{" ".join(lst)}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
