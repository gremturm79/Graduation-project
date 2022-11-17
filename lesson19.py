from random import *


def slicer(x, tpl):
    if tpl.count(x) == 0:
        tpl = list(tpl)
        del tpl[0:len(tpl) + 1]
        tpl = tuple(tpl)
        return tuple(tpl)
    elif tpl[i] == x and tpl.count(x) == 1:
        return tpl[i:]
    elif tpl[i] == x and tpl.count(x) == 2:
        index1 = tpl.index(x)
        index2 = tpl.index(x, index1 + 1)
        return tpl[index1:index2 + 1]


tpl_1 = tuple(randint(0, 15) for i in range(1, 15))
a = int(randint(0, 15))
print('Случайный список', tpl_1)
print('Случайный элемент: ', a)
print('Новый список:', slicer(a, tpl_1))
