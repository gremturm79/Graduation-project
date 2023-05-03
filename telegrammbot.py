
import time
import logging
from aiogram import Bot, Dispatcher, executor, types
from weather import Weather
from translate import Translator

TOKEN = '5760389963:AAESPX0gp8CXs2fOFg84gj0zegV2NDySgOg'
MSG = 'Как дела, {}?'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

translator = Translator(from_lang='en', to_lang='ru')
reg = r'[A-z]'


@dp.message_handler()
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f'Привет, {message.from_user.full_name}, погода в {message.text}')
    translator1 = Translator(from_lang='ru', to_lang='en')
    translation = translator1.translate(message.text)
    weather = Weather(temperature_unit='Celsius')
    current_weather = weather.fetch_weather(translation, only_temp=True)
    lst = []
    for i in current_weather:
        if i == 'Pressure: ':
            current_weather[i] *= 0.76
        lst.append(str(i))
        lst.append(str(current_weather[i]))
        lst.append('||')

    # lst = list(map(str, lst))
    for i in range(len(lst)):
        if i == 4:
            continue
        lst[i] = translator.translate(lst[i])
    lst = ' '.join(lst)
    await message.reply(f'{lst}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
