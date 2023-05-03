a = int(input('Введите ширину: '))
b = int(input('Введите высоту: '))

i = 1
j = 1
for i in range(a):
    print('\n', end='')
    if i % 2 == 0:
        print('*', end='')
    for j in range(b):
        print('*', end='')
