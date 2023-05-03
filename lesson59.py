import requests  # импортируем библиотеку requests
import re # импортируем библиотеку для регулярных выражений

url = input('Введите ссылку: ')  # поиск в определённой зоне

html_text = requests.get(url).text  # делаем запрос и получаем html

reg = r'[^"]\w+://\w\.\w+\.\w+/\w/\d+\.mp3'
url1 = re.findall(reg, html_text, flags=re.MULTILINE)
r = requests.get(url1[0])
str1 = input('Сохранить как: ')
with open(str1 + '.mp3', 'wb') as f:
    f.write(r.content)
f.close()

import pyglet
import time
time1 = int(input('Введите количество минут:'))
time1 *= 60
time.sleep(time1)
song = pyglet.media.load('C:\\mp3\\1.mp3')
song.play()
pyglet.app.run()