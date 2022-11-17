from random import *

w = 4
h = 3
lst = [[randint(0, 10) for j in range(w)] for i in range(h)]
print(lst)
for row in range(len(lst)):
    for col in range(len(lst[row])):
        print(lst[row][col], end='  ')
    print()
print()
lst_1 = []
for row in range(len(lst)+1):
    for col in range(len(lst)):
        print(lst[col][row], end='  ')
    print()

