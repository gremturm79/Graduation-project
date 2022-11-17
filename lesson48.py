import re

lst = []
lst1 = []


def checking(a):
    start = 6
    finish = 18
    check = ''.join(re.findall(r'^[\d*A-z_@-]{6,18}$', a))
    if start > len(password):
        print('Пароль слишком короткий')
    elif finish < len(password):
        print('Пароль слишком длинный')
    elif check == password:
        print(f'Введённый пароль {password} подходит: ')
    elif check != password:
        for i in range(len(password)):
            if password[i] not in check:
                lst.append(password[i])
                break
            else:
                lst1.append(password[i])
        print('Пароль не прошёл проверку присутствует не допустимый символ', ''.join(lst))


# print(re.findall(r'[\d*A-z_@-]{6,18}', a))


password = input('Введите пароль: ')
checking(password)
