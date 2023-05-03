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


class Rectangle(Shape):
    '''
       Класс Rectangle принимает 2 свойства long, width и наследует свойство color класса Shape. Имеет 4 метода area,
       perimetr, paint_shape, info соответственно для вычисления площади, периметра, графического отображения фигуры,
      и вывод информации со всеми данными вычисления
    '''

    def __init__(self, color, long, width):
        if isinstance(long, (int, float)) and isinstance(width, (int, float)):
            self.long = long
            self.width = width
        else:
            raise TypeError('данные должны быть типом int')
        super().__init__(color)

    def area(self):
        return f'Площадь: {self.long * self.width}'

    def perimetr(self):
        return f'Периметр: {(self.long + self.width) * 2}'

    def paint_shape(self):
        for i in range(self.width):
            for j in range(self.long):
                print('*', end='  ')
            print()

    def info(self):
        print('Прямоугольник'.center(20, '='))
        print(f'Длина: {self.long}')
        print(f'Ширина: {self.width}')
        print(f'Цвет: {self.color}')
        print(f'{self.area()}')
        print(f'{self.perimetr()}')
        return self.paint_shape()