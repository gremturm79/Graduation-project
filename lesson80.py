import requests
from bs4 import BeautifulSoup


class Auto:
    '''
    Класс Auto предназначен для учета данных автомобиля
    имеет property методы set и get, соответственно для получения значения и установки значения всех свойств
    экземпляра класса
    имеет staticmethod методы для проверки инициализации свойств экземпляра класса
    имеет метод класса print_info вывода в консоль значения всех свойств экземпляра класса
    '''
    check = 'auto'
    unit_power = 'л.с'
    lst = []

    def __init__(self, model, year, producer, power, color, price):
        self.model = model
        self.year = year
        self.producer = producer
        self.power = power
        self.color = color
        self.price = price

    @staticmethod
    def check_model(model):
        if not isinstance(model, str):  # метод проверки значения свойства model на тип данных str
            raise TypeError('значение должно быть строкой')

    @staticmethod
    def check_year(year):  # метод проверки значения свойства year на тип данных str и диапазон
        if not isinstance(year, int) or not 1950 < year < 2023:
            raise TypeError('значение должно быть числом и не превышать диапазон 1950-2022')

    @staticmethod
    def check_producer(producer):
        if not isinstance(producer, str):
            raise TypeError('значение должно быть строкой')

    def check_list_auto(self, producer):  # метод проверки на существования производителя через парсинг сайта
        url = requests.get('https://m3-spb.ru/cars')  # делаем запрос на сайт получаем HTML страницу
        soup = BeautifulSoup(url.content, 'html.parser')  # сохраняем код в переменной в виде HTML кода
        soup1 = soup.findAll('a', class_='cars__popular__text')  # отбираем все родительские теги с классом в которых
        # находятся названия автомобилей
        for el in range(len(soup1)):
            self.lst.append(soup1[el].findNext('span').text)  # получение из дочернего тега span его значения
            # добавление их в список lst (названия автомобилей)
        if self.lst.count(producer) < 1:  # проверка на нахождение в списки названия автомобиля
            raise TypeError('такого производителя нет')

    @staticmethod
    def check_power(power):  # метод проверки значения свойства power на тип данных int
        if not isinstance(power, int):
            raise TypeError('значение должно быть числом')

    @staticmethod
    def check_color(color):  # метод проверки значения свойства color на тип данных str
        if not isinstance(color, str):
            raise TypeError('значение должно быть строкой')

    @staticmethod
    def check_price(price):  # метод проверки значения price на тип данных int
        if not isinstance(price, int):
            raise TypeError('значение цены должно быть числом')

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.check_model(model)
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.check_year(year)
        self.__year = year

    @property
    def producer(self):
        return self.__producer

    @producer.setter
    def producer(self, producer):
        self.check_producer(producer)
        self.check_list_auto(producer)
        self.__producer = producer

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        self.check_power(power)
        self.__power = power

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.check_color(color)
        self.__color = color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.check_price(price)
        self.__price = price

    def print_info(self):
        print(f'Данные автомобиля'.center(40, '*'))
        print(f'Название модели: {self.__model}')
        print(f'Год выпуска {self.__year}')
        print(f'Производитель: {self.__producer}')
        print(f'Мощность двигателя: {self.__power}')
        print(f'Цвет машины: {self.__color}')
        print(f'Цена {self.__price}')


auto = Auto('X70 M50i', 2021, 'BMW', 530, 'white', 10790000)
auto.model = 'Typo'
auto.year = 2005
auto.power = 300
auto.producer = 'Cadillac'
auto.color = 'red'
auto.price = 6000000
auto.print_info()

auto1 = Auto('Ч5', 2010, 'Газ', 120, 'Чёрный', 5000000)
# auto1.model = 'Typo'
# auto1.year = 2005
# auto1.power = 300
auto1.producer = 'Changan'
# auto1.color = 'red'
# auto1.price = 6000000
auto1.print_info()
