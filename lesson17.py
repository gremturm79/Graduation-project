from random import *

h = 6
w = 6
lst = [[randint(0, 10) for j in range(w)] for i in range(h)]

for row in range(len(lst)):
    for col in range(len(lst[row])):
        print(lst[row][col], end='   ')
    print()
print()
lst_2 = [randint(0, 10) for k in range(h)]
print(lst_2)
print()
for row in range(len(lst)):
    for col in range(len(lst[row])):
        if row % 2 == 0:
            for j in range(len(lst)):
                lst[row][j] = lst_2[j]
            print(lst[row][col], end='   ')
        else:
            print(lst[row][col], end='   ')
    print()
