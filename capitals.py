import json


class Capital:
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
    def dict_edit(keys, values):
        Capital.dict_capital[keys] = values
        # return Capital.dict_capital  # необязательно

    @staticmethod  # серелизация словаря в json объект с сохранением в файл dict_capitals.json
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


Capital.dict_app('Россия', 'Москва')
Capital.dict_app('Франция', 'Париж')
Capital.show_dict()
Capital.dict_app('Италия', 'Рим')
Capital.show_dict()
Capital.dict_coder()
print(Capital.dict_decoder())