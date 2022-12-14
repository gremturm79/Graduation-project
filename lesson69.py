import math


class Area:
    '''
    Класс Area имеет статическое свойство count для подсчёта количество вхождений в класс.
    Также в нём находятся такие методы как: площадь треугольника по методу Герона, площадь треугольника через основание
    и высоту, площадь квадрата, площади прямоугольника, и метод подсчёта количества использования этих методов.
    '''

    count = 0

    @staticmethod
    def checking(i):
        if isinstance(i, (int, float)):
            return True
        return False

    @staticmethod
    def triangle_gerona(a, b, c):  # метод вычисления площади треугольника по формуле Герона
        if Area.checking(a) and Area.checking(b) and Area.checking(c):
            Area.count += 1
            p = (a + b + c) // 2
            return f'Площадь треугольника по методу Герона ({a},{b},{c}): {round(math.sqrt(p * ((p * 3) - (a + b + c))), 2)}'

    @staticmethod
    def triangle_height(hypotenuse, height):  # метод вычисления площади треугольника по основанию и высоте
        if Area.checking(hypotenuse) and Area.checking(height):
            Area.count += 1
            return f'Площадь треугольника через основание и высоту ({hypotenuse},{height}): {(hypotenuse * height) / 2}'
        else:
            return f'Для нахождения площади треугольника необходимо 2 числа'

    @staticmethod
    def square(a):  # метод вычисления площади квадрата
        if Area.checking(a):
            Area.count += 1
            return f'Площадь квадрата ({a}): {a * a}'
        else:
            return f'Для нахождения площади квадрата необходимы числа'

    @staticmethod
    def rectangle(a, b):  # метод вычисления площади прямоугольника
        if Area.checking(a) and Area.checking(b):
            Area.count += 1
            return f'Площадь прямоугольника ({a},{b}): {a * b}'
        else:
            return f'Для вычисления площади прямоугольника необходимо 2 числа'

    @staticmethod
    def count_method():  # метод количества подсчёта площадей
        return f'Количество подсчётов площади: {Area.count}'


p1 = Area()
print(Area.triangle_gerona(3, 4, 5))
print(p1.triangle_height(6, 7))
print(p1.square(7))
print(Area.rectangle(2, 6))
print(p1.count_method())
