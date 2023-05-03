import json


class Capital:
    '''
    Класс Capital имеет два принимающих в аргументах свойства country и capitals из которых собирается словарь
    dict_capital. Класс имеет методы: show_dict для просмотра данных словаря, dict_app добавление данных в словарь,
    dict_del удаление данных из словаря, dict_find поиск данных по словарю, dict_edit редактирование значений
    по их ключу,dict_coder сереализация словаря в json объект с сохранением в файл dict_capitals.json,
    dict_decoder сереализация словаря в json объект с сохранением в файл dict_capitals.json
    '''
    dict_capital = dict()

    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
        Capital.dict_capital = {self.country: self.capital}

    def __str__(self):
        return f'Страна: {self.country}  столица: {self.capital}'

    @staticmethod
    def show_dict():  # просмотр данных словаря
        print(f'Словарь столиц мира:  {Capital.dict_capital} ')

    @staticmethod
    def dict_app(country, capitals):  # добавление данных в словарь
        Capital.dict_capital[country] = capitals
        return Capital.dict_capital

    @staticmethod
    def dict_del(keys):  # удаление данных из словаря
        Capital.dict_capital.pop(keys)
        return Capital.dict_capital

    @staticmethod
    def dict_find(keys):  # поиск данных по словарю
        print(f'Столица {keys} является {Capital.dict_capital[keys]}')

    @staticmethod
    def dict_edit(keys, values):  # редактирование значений по их ключу
        try:
            Capital.dict_capital[keys] = values
        except KeyError:
            return f'ключ {keys}, неизвестен'
        # return Capital.dict_capital  # необязательно

    @staticmethod  # сереализация словаря в json объект с сохранением в файл dict_capitals.json
    def dict_coder():
        # try:
        # file1 = json.load(open('dict_capitals.json'))
        # except FileNotFoundError:
        # file1 = dict()
        with open('dict_capitals.json', 'w') as file:
            json.dump(Capital.dict_capital, file, indent=2, ensure_ascii=True)
            return file

    @staticmethod  # десериализация файла dict_capitals.json в файл '.py'
    def dict_decoder():
        with open('dict_capitals.json', 'r') as file:
            d_read = json.load(file)
            return d_read


text = ['Выбор действия:', '1-добавление данных', '2-удаление данных', '3-поиск данных', '4-редактирование данных',
        '5-просмотр данных', '6-завершение работы']


def road():
    print('*' * 20)
    for i in text:
        print(i)
    print('*' * 20)
    d = int(input('Введите число для действия: '))
    if d == 1:
        country = input('Введите название страны (с заглавной буквы): ')
        capital = input('Введите название столицы (с заглавной буквы): ')
        Capital.dict_app(country, capital)
        Capital.dict_coder()
        print(f'{country} и {capital} успешно добавлены в словарь')
        road()
    elif d == 2:
        country = input('Введите название страны, для удаления из словаря (с заглавной буквы): ')
        try:
            Capital.dict_del(country)
            Capital.dict_coder()
            print(f'Страна {country} успешна удалена из файла')
            road()
        except KeyError:
            print('Ошибка ключа')
            road()
    elif d == 3:
        country = input('Введите название страны, для поиска в словаре (с заглавной буквы): ')
        try:
            Capital.dict_find(country)
            road()
        except KeyError:
            print(f'{country} такой страны нет в словаре')
            road()
    elif d == 4:
        country = input('Введите название страны (с заглавной буквы): ')
        capital = input('Введите название столицы (с заглавной буквы): ')
        Capital.dict_edit(country, capital)
        Capital.dict_coder()
        print('Словарь успешно исправлен')
        road()
    elif d == 5:
        print(Capital.dict_decoder())
        road()
    elif 1 > d >= 6:
        print('неправильный ввод командной строки')
        raise ValueError('неправильный ввод командной строки')
    else:
        print('Вы вышли из программы')


road()
