class Figure:
    def __init__(self, color):
        self.__color = color

    def __str__(self):
        return f'{self.__color}'

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


class Rectangle(Figure):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def __str__(self):
        return f'{self.__width} {self.__height} {self.color}'

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if width > 0:
            self.__width = width
        else:
            raise TypeError('Ширина должна быть положительным числом')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height > 0:
            self.__height = height
        else:
            raise TypeError('Высота должна быть положительным числом')

    def area(self):
        return self.__height * self.__width


rect = Rectangle(10, 20, 'green')

rect.width = 5
rect.height = 10
print(rect)
print(rect.area())

