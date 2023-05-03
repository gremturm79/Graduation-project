wort = 'Копе'

d = int(input('Введите число от 0 до 99: '))
if 0 > d > 100:
    print('Неверный формат')
elif d == 1 or d % 10 == 1:
    print(d, wort + 'йка')
elif d == 0 or 5 <= d <= 15:
    print(d, wort + 'ек')
elif 4 >= d <= 2 or d % 10 == 2 or d % 10 == 3 or d % 10 == 4:
    print(d, wort + 'йки')
else:
    print(d, wort + 'ек')

a, b = 20, 20
minim = a if a < b else b
print(minim)

a, b = 20, 20
print('a == b' if a == b else 'a > b' if a > b else 'a < b')

g = int(input('Введите цифру'))
j = int(input('Введите цифру'))
print('На ноль делить нельзя' if j == 0 else g // j)




