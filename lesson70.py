class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __check_value(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    def set_coord(self, x, y):
        if Point.__check_value(x) and Point.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            print('Координаты должны быть числами')

    def get_coord(self):
        return self.__x, self.__y


p1 = Point(1, 3)
print(p1.__dict__)
p1.set_coord(1, 3)
print(p1.get_coord())

print(Point.__doc__)
