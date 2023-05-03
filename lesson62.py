import requests


url = 'https://s.voicecards.ru/c/15503.mp3'
r = requests.get(url)

with open('1.mp3', 'wb') as f:
    f.write(r.content)

print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)