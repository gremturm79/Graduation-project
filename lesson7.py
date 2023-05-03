a = [int(input('Введите значение элемента: ')) for i in range(int(input('Введите количество элементов: ')))]
for i in range(len(a)):
    if a[i] > a[i-1]:
        print(a[i], end=' ')