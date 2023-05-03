import math


class Rectangle:
    '''
    Класс Rectangle принимает свойства два свойства типа данных int: long, и wide. Имеет методы для расчёта площади,
    периметра, гипотенузы прямоугольника, а также метод который выводит прямоугольник графически элементами '*'.
    '''

    def __init__(self, long, wide):  # инициализация свойств экземпляра
        self.__long = long  # Длина прямоугольника
        self.__wide = wide  # Ширина прямоугольника

    def set_long(self, long):  # метод установки длины прямоугольника
        self.__long = long

    def get_long(self):  # метод получения значения длины прямоугольника
        print(f'Длина прямоугольника: {self.__long}')

    def set_wide(self, wide):  # метод установки ширины прямоугольника
        self.__wide = wide

    def get_wide(self):  # метод получения значения ширины прямоугольника
        print(f'Ширина прямоугольника: {self.__wide}')

    def sqr_rectangle(self):  # метод получения площади прямоугольника
        return f'Площадь прямоугольника: {self.__long * self.__wide}'

    def perimetr_rectangle(self):  # метод получения периметра прямоугольника
        return f'Периметр прямоугольника: {(self.__long + self.__wide) * 2}'

    def hypotenuse_rectangle(self):  # метод получения гипотенузы прямоугольника
        return f'Гипотенуза прямоугольника: {round(math.sqrt(math.pow(self.__long, 2) + math.pow(self.__wide, 2)), 2)}'

    def visual_rectangle(self):  # метод получения графической визуализации прямоугольника
        print(f'Визуализация прямоугольника'.center(33, '-'))
        for i in range(self.__long):
            for j in range(self.__wide):
                print('*  ', end='')
            print()
        # self.visual = [['*' for j in range(self.wide)] for i in range(self.long)]
        # return '\n'.join(list('   '.join(self.visual[i]) for i in range(len(self.visual))))


p1 = Rectangle(3, 9)
p1.set_long(4)
p1.set_long(7)
p1.get_long()
p1.get_wide()
print(p1.sqr_rectangle())
print(p1.perimetr_rectangle())
print(p1.hypotenuse_rectangle())
p1.visual_rectangle()






