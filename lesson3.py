crown = int(input('Введите количество ворон :'))
if 0 <= crown <= 9:
    print('На ветке', end=' ')
    if crown == 1:
        print(crown, 'ворона')
    elif 2 <= crown <= 4:
        print(crown, 'вороны')
    else:
        print(crown, 'ворон')

else:
    print('Ошибка ввода данных')














