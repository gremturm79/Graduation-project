import math


class Table:
    '''
    Класс Table имеет два дочерних класса RectTable и CircleTable, в которых есть методы для вычисления площадей
    CircleTable имеет метод для вычисления площади круглого стола, RectTable имеет метод для вычисления площади
    прямоугольного и квадратного стола при отсутствии свойства long
    '''

    def __init__(self, width=None, long=None, radius=None):
        self._width = width
        self._long = long
        self._radius = radius

    @property
    def get_width(self):
        return self._width

    @get_width.setter
    def get_width(self, width):
        if self.is_int():
            self._width = width

    @property
    def get_long(self):
        return self._long

    @get_long.setter
    def get_long(self, long):
        if self.is_long():
            self._long = long

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if self.is_int():
            self._radius = radius

    def is_long(self):  # проверка свойства long
        if self._long is not None and isinstance(self._long, (int, float)) and self._long > 0:
            return True
        print('значение должны быть числом и больше 0')
        return False

    def is_int(self):
        if not isinstance(self._width, (int, float)) and not isinstance(self._radius, (int, float)):
            print(f'значения должны быть числами')
            return False
        return True

    def area(self):  # абстрактный метод
        raise NotImplemented('В дочернем классе должен быть определён метод area()')


class RectTable(Table):
    # метод расчёта площади прямоугольного стола, при отсутствии аргумента long этот аргумент принимает свойство width
    def area(self):
        if self._long is None:
            self._long = self._width
            if self.is_int():
                print(self.__dict__)
                return self._long * self._width
        else:
            if self.is_long():
                print(self.__dict__)
                return f'{self._width * self._long}'  # расчёт площади при наличии двух свойств


class CircleTable(Table):  # дочерний класс, родительский класс Table
    def area(self):  # метод расчёта площади круглого стола
        if self.is_int():
            print(self.__dict__)
            return round(math.pi * math.pow(self._radius, 2), 2)
        else:
            raise TypeError('значения должны быть числами')


table1 = RectTable(20)  # экземпляр класса при условии одного заданного аргумента
print(table1.area())
table1.get_long = 10
print(table1.area())  # экземпляр класса при условии двух заданных аргументов
table = CircleTable(5)  # экземпляр класса круглого стола
table.radius = 20  # установка свойства radius
print(table.area())
# print(Table.area(table))
# table1.get_width = 6
# print(table1.get_long)
# table1.get_width = 6
# table1.get_long = 6
# table3 = Table(7, 7, 7)
# print(table3.area())
