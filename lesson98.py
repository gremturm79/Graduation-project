class CheckSideTriangle:
    '''
    Класс CheckSideTriangle является дескриптором, имеет метод __set__  для установки значений свойств
    с проверкой на тип данных int и проверки свойства требующее значение больше ноля
    '''
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if isinstance(value, int) and value > 0:
            instance.__dict__[self.name] = value
        else:
            raise TypeError(f'тип данных свойства должен быть int и положительным числом')


class Triangle:
    '''
    Класс Triangle принимает три свойства: длины сторон треугольника side1, side2, side3. Имеет метод проверки
    существования треугольника check_triangle. Имеет проверку свойств через дескриптор CheckSideTriangle.
    '''
    side1 = CheckSideTriangle()
    side2 = CheckSideTriangle()
    side3 = CheckSideTriangle()

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def check_triangle(self):  # функция проверки существования треугольника
        if self.side1 + self.side2 <= self.side3:
            return f'Треугольника сo сторонами {self.side1} ,{self.side2} ,{self.side3}  не может существовать'
        elif self.side2 + self.side3 <= self.side1:
            return f'Треугольника сo сторонами {self.side1} ,{self.side2} ,{self.side3} не может существовать'
        elif self.side1 + self.side3 <= self.side2:
            return f'Треугольника co сторонами {self.side1} ,{self.side2} ,{self.side3} не может существовать'
        else:
            return f'Треугольник со сторонами {self.side1} ,{self.side2} ,{self.side3} существует'


t = Triangle(2, 5, 6)
t1 = Triangle(5, 2, 8)
t2 = Triangle(7, 3, 6)
print(t.check_triangle())
print(t1.check_triangle())
print(t2.check_triangle())
