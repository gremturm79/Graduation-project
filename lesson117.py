import requests
import fake_useragent

ua = fake_useragent.UserAgent()
headers = {
    'User-Agent': ua.random
}
response = requests.get('https://bookriver.ru/reader/sonya-marey-doktora-vyzyvali-ili-trudovye-budni-popadanki/448929',
                        headers=headers)
print(response.text)

# with open('Дуглас Адамс. Детективное агентство Дирка Джентли.txt', 'w') as file:
# for piece in response.iter_content(chunk_size=5000):
# print('piece write')
# file.write(piece.decode(response.encoding))
