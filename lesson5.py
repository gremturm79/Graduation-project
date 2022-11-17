a = int(input('Введите число: '))
b = int(input('Введите число: '))

if a < b and a % 2 != 0:
    for i in range(a, b + 1, 2):
        print(i, end=' ')
    else:
        print('-- Результат диапазона нечётных чисел от', a, 'до', b)
elif a < b and a % 2 == 0:
    for i in range(a+1, b + 1, 2):
        print(i, end=' ')
    else:
        print('-- Результат диапазона нечётных чисел от', a, 'до', b)
elif a > b and b % 2 != 0:
    for i in range(b, a + 1, 2):
        print(i, end=' ')
    else:
        print('-- Результат диапазона нечётных чисел от', a, 'до', b)
elif a > b and b % 2 == 0:
    for i in range(b+1, a + 1, 2):
        print(i, end=' ')
    else:
        print('Результат диапазона нечётных чисел от', a, 'до', b)