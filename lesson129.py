import requests


s = 'https://fs.kinomania.ru/image/file/news/7/81/7814d6c5454757a2032524be9faaf02f.365.199.jpeg'

with open('pic1.jpg', 'wb') as handle:
    response = requests.get(s, stream=True)

    if not response.ok:
        print(response)
    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)


