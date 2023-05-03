import logging
from aiogram import Bot, Dispatcher, types, executor
import time
import requests
from bs4 import BeautifulSoup

TOKEN = '5760389963:AAESPX0gp8CXs2fOFg84gj0zegV2NDySgOg'
MSG = 'как дела {} ?'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler()
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    # user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f'Привет, {message.from_user.full_name}, свежие новости {message.text}')
    url = requests.get('https://klops.ru')
    soup = BeautifulSoup(url.text, 'html.parser')
    soup1 = soup.findAll(class_='title')
    soup2 = soup.findAll(class_='item')
    lst = []
    i = 0
    while i < 5:  # 35 all elements
        lst.append(soup1[i + 1].text)
        lst.append(soup2[i].get('href'))

        i += 1
    for i in range(len(lst)):
        await message.reply(lst[i])
    # lst = ''.join(lst)






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
