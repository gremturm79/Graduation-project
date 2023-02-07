import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):  # функция делает запрос на страницу сайта и получает данные в виде html кода
    url = requests.get(url)
    return url.text


def write_csv(data):  # функция создаёт файл csv и записывает в него данные в формате csv приходящие в параметр data
    with open('kino.csv', 'a', encoding='utf-8') as file:
        write = csv.writer(file, lineterminator='\r', delimiter=';')
        write.writerow((data['name'], data['description'], data['views']))


def get_data(html):  # функция парсит данные с сайта, записывает их в словарь и передаёт их в функцию write_csv
    soup = BeautifulSoup(html, features='lxml')
    name_film = soup.find_all('font', {'color': '#E3E3E3'})
    description_film = soup.find_all('div', class_="rt-article-content")
    views_films = soup.find_all('span', class_='rt-author')
    d = {}
    for i, j, k in zip(name_film, description_film, views_films):
        d = {
            'name': i.text,
            'description': j.text.strip()[:150] + '...',
            'views': k.find_next('span').text
        }
        write_csv(d)


def main():  # функция возвращает вызов функции get_data и передаёт параметр в неё параметр
    for i in range(1, 5):
        url = f'http://tvklik.ru/load/novinki/100-{i}'
        get_data(get_html(url))


# запуск программы
if __name__ == '__main__':
    main()
