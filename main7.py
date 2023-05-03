import math
from random import *


def test(tpl, a):
    for i in tpl:
        if i % a == 0:
            d.append(i)
    set(d)
    if max(d) <= 0:
        return 'no num'
    else:
        return max(d)


d = []
num = 13
u = [2, 7, 0, 3, 1, 5, -13]
h = [2, 7, 0, 3, 1, 5, -13, 13]
m = [26]
k = [99, 99, 100, 34, -39]
g = [99, 39, 99, 100, 34]

print('Наибольшее положительное значение кратное 13: ', test(g, num))

