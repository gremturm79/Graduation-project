import time
import logging
from aiogram import Bot, Dispatcher, executor, types
from OpenweatherPy import WeatherPy
from translate import Translator

TOKEN = '5760389963:AAESPX0gp8CXs2fOFg84gj0zegV2NDySgOg'
MSG = 'Как дела, {}?'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

translator = Translator(from_lang='en', to_lang='ru')

weather = WeatherPy('8eb0ec61db7b93e0eb2c74716c8e6c8f')


@dp.message_handler()
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f'Привет, {message.from_user.full_name}, погода в {message.text}')
    translator1 = Translator(from_lang='ru', to_lang='en')
    city2 = translator1.translate(message.text)
    city = weather.query(city=city2)
    city1 = translator.translate(city.name)
    t = city.temperature - 273, 15
    t1 = round(t[0], 1)
    d = city.pressure / 1.3
    d1 = round(d, 1)
    w = city.wind
    w1 = w['speed']
    a = ['город:', city1, '\n']
    b = ['температура:', t1, '\n']
    c = ['влажность:', city.humidity, '\n']
    d = ['давление:', d1, '\n']
    e = ['cкорость ветра:', w1, '\n']
    lst = a + b + c + d + e
    lst1 = list(map(str, lst))
    forecast = ' '.join(lst1)

    await message.reply(f'{forecast}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
