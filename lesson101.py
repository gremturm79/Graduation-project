import math


class Shape:
    '''
    Класс Shape принимает одно свойство color, содержит: 4 абстрактных метода area, perimetr, paint_shape, info.
    Также имеет три дочерних класса: Square, Rectangle, Triangle
    '''

    def __init__(self, color):
        if isinstance(color, str):
            self.color = color
        else:
            raise TypeError('данные должны быть типом str')

    def area(self):
        raise NotImplemented('метод должен быть реализован в дочернем классе')

    def perimetr(self):
        raise NotImplemented('метод должен быть реализован в дочернем классе')

    def paint_shape(self):
        raise NotImplemented('метод должен быть реализован в дочернем классе')

    def info(self):
        raise NotImplemented('метод должен быть реализован в дочернем классе')


class Square(Shape):
    '''
    Класс Square принимает свойство side и наследует свойство color класса Shape. Имеет 4 метода area, perimetr,
    paint_shape, info соответственно для вычисления площади, периметра, графического отображения фигуры, и вывод
     информации со всеми данными вычисления
    '''

    def __init__(self, color, side):
        if isinstance(side, (int, float)):
            self.side = side
        else:
            raise TypeError('данные должны быть типом int')
        super().__init__(color)

    def area(self):  # метод расчёта площади квадрата
        return f'Площадь: {self.side * 2}'

    def perimetr(self):  # метод расчёта периметра квадрата
        return f'Периметр: {self.side * 4}'

    def paint_shape(self):  # метод графической визуализации квадрата
        for i in range(self.side):
            for j in range(self.side):
                print('*', end='  ')
            print()

    def info(self):  # метод вывода информации
        print('Квадрат'.center(20, '='))
        print(f'Сторона: {self.side}')
        print(f'Цвет: {self.color}')
        print(f'{self.area()}')
        print(f'{self.perimetr()}')
        return self.paint_shape()


__author__ = 'Alex'

if __name__ == '__main__':
    print(f'{__name__}, {__author__}')

