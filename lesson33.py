s = None


def func(a, b, c):
    s = 1
    s = (a * b + a * c + b * c) * 2
    print('Площадь параллелепипеда', s)

    def rectangle(a, b):
        nonlocal s
        s = 1
        s = a * b
        print('Площадь прямоугольника', s)

    return rectangle


func(2, 4, 6)
func(5, 8, 2)
func(1, 6, 8)
