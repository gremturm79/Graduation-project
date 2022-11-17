a = int(input('Высота прямоугольника: '))
b = int(input('Длина прямоугольника: '))
i = 1
for u in range(a):
    for i in range(b):
        for j in range(a):
            for k in range(b):
                if (u + j) % 2 != 0:
                    print('*'' ', end='')
                else:
                    print(' '' ', end='')
        print()
