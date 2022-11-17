from random import *
lst = []
a = int(input('Введите количество элементов: '))
print('Введите элементы списка: ')
print('n =', a)
i = 0
while i != a:
    j = int(input('-> '))
    lst.append(j)
    i += 1
k = int(input('Введите значение чтобы удалить: '))
print('k =', k)
lst.remove(k)
lst.sort(reverse=True)
print(lst)
