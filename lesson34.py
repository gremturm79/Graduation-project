s = None
a = int(input('->'))
b = int(input('->'))
c = int(input('->'))


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


# res1 = func(2, 4, 6)
# res1(2, 4)
# res2 = func(5, 8, 2)
# res2(5, 8)
# res3 = func(1, 6, 8)
# res3(1, 6)
res5 = func(a, b, c)
res5(a, b)
