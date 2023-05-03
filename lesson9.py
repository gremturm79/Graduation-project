a = [int(input('->')) for i in range(int(input('Введите количество элементов:  ')))]
ch = int(input('Введите число: '))
print('ch =', ch)
for i in a:
    if i == ch:
        print('Число', ch, 'присутствует в элементах списка')
