# class Vector(list):
# def __str__(self):
# return ' '.join(map(str, self))


# v = Vector([1, 2, 3])
# print(v)
# print(type(v))
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def is_int(self):
        if not isinstance(self.__x, int) or not isinstance(self.__y, int):
            print(f'Координаты должны быть целочисленными')
            return False
        return True


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def set_coord(self, sp, ep):
        if sp.is_int() and ep.is_int():
            self._sp = sp
            self._ep = ep


class Line(Prop):
    def draw_line(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")

    def set_coord(self, sp, ep=None):
        if ep is None:
            if sp.is_int():
                self._sp = sp
        else:
            if sp.is_int() and ep.is_int():
                self._sp = sp
                self._ep = ep


line = Line(Point(1, 2), Point(10, 20))
line.set_coord(Point(20, 40), Point(50, 60))
line.draw_line()
line.set_coord(Point(200, 400))
line.draw_line()


