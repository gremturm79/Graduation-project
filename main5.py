from random import *
tpl = tuple(randint(0, 15) for i in range(0, 10))
print('Случайный кортеж: ', tpl)
d = 10
print('Искомый элемент: ', d)
if d in tpl:
    print('YES')
else:
    print('NO')
