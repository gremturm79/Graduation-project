class Rect:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def show_rect(self):
        print(f'Прямоугольник:\nШирина: {self.__width}\nВысота:{self.__height}')


class RectFon(Rect):
    def __init__(self, width, height, background):
        self.__background = background
        super().__init__(width, height)

    def show_rect(self):
        super().show_rect()
        print(f'Фон, {self.__background}')


class RectFonBorder(RectFon):
    def __init__(self, width, height, background, border):
        self.__border = border
        super().__init__(width, height, background)

    def show_rect(self):
        super().show_rect()
        print(f'Рамка {self.__border}')


# class RectBorder(Rect):
# def __init__(self,  width, height, border):
# self.__border = border
# super().__init__(width, height)

# def show_rect(self):
# super().show_rect()
# print(f'Рамка {self.__border}')


shape = Rect(100, 200)
shape.show_rect()
shape1 = RectFon(400, 300, 'yellow')
shape1.show_rect()
shape3 = RectFonBorder(20, 30, 'yellow', '1px solid red')
shape3.show_rect()
