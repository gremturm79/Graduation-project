import re

lst = []
lst1 = []


def checking(a):
    # global i
    start = 6
    finish = 18
    check = ''.join(re.findall(r'[\dA-z@-]{6,18}', a))
    print(check)
    if start > len(password):
        print('Пароль слишком короткий')
    elif finish < len(password):
        print('Пароль слишком длинный')
    elif check == password:
        print(f'Введённый пароль {password} подходит: ')
    if check == password:
        print(f'Введённый пароль {password} подходит ')
    elif check != password:
        for i in range(len(password)):
            if password[i] not in check:
                lst.append(password[i])
                print(lst)
                break
            else:
                lst1.append(password[i])
        print('Введённый пароль', password,  'не подходит присутствует недопустимый символ', ''.join(lst))

    # print(re.findall(r'[\d*A-z_@-]{6,18}', a))


password = input('Введите пароль: ')
checking(password)







