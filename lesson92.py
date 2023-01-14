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


class Triangle(Shape):
    '''
    Класс Triangle принимает 3 свойства side, side1, side2 и наследует свойство color класса Shape. Имеет 4 метода
    area, perimetr, paint_shape, info соответственно для вычисления площади, периметра,графического отображения фигуры,
     и вывод информации со всеми данными вычисления
    '''

    def __init__(self, color, side, side1, side2):
        self.side = side
        self.side1 = side1
        self.side2 = side2
        super().__init__(color)

    def area(self): # метод расчёта площади треугольника по формуле Герона
        if self.side + self.side1 <= self.side2:
            print(f'Треугольника с такими сторонами не может существовать')
        if self.side + self.side2 <= self.side1:
            print(f'Треугольника с такими сторонами не может существовать')
        if self.side1 + self.side2 <= self.side:
            print(f'Треугольника с такими сторонами не может существовать')
        else:
            p = (self.side + self.side1 + self.side2) / 2
            s = math.sqrt(p * (p - self.side) * (p - self.side1) * (p - self.side2))
            return f'Площадь: {round(s, 2)}'

    def perimetr(self):
        return f'Периметр: {self.side + self.side1 + self.side2}'

    def paint_shape(self):
        if self.side + self.side1 <= self.side2:
            print(f'Треугольника с такими сторонами не может существовать')
        if self.side + self.side2 <= self.side1:
            print(f'Треугольника с такими сторонами не может существовать')
        if self.side1 + self.side2 <= self.side:
            print(f'Треугольника с такими сторонами не может существовать')
        else:
            for i in range(self.side1):
                for j in range(0, self.side):
                    print(end=' ')
                self.side -= 1
                for j in range(0, i + 1):
                    print('*', end=' ')
                print(' ')
            print(f'С новым годом!!!'.upper().center(30, '*'))

    def info(self):
        print('Треугольник'.center(20, '='))
        print(f'Сторона1: {self.side}')
        print(f'Сторона2: {self.side1}')
        print(f'Сторона3: {self.side2}')
        print(f'Цвет: {self.color}')
        print(f'{self.area()}')
        print(f'{self.perimetr()}')
        return self.paint_shape()


p1 = Shape('green')
p2 = Square('red', 5)
p3 = Rectangle('green', 6, 5)
p4 = Triangle('red', 11, 6, 6)

lst = [p2, p3, p4]
for i in lst:
    i.info()
