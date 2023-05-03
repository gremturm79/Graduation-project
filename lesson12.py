from random import *

n1 = int(input('Введите количество элементов: '))
n2 = int(input('Введите количество элементов: '))
a = [randint(0, 10) for i in range(n1)]
b = [randint(0, 10) for j in range(n2)]
print(a)
print(b)
c = a + b
print(c)
c = []
for i in range(len(a)):
    if a[i]not in b:
        c.append(a[i])
for i in range(len(b)):
    if b[i] not in c:
        c.append(b[i])
print(c)
c = []
for i in range(len(a)):
    if a[i] in b and a[i] not in c:
        c.append(a[i])
print(c)
print(min(a), max(a), ':', min(a), max(a))
