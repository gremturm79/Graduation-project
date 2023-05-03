from random import *


def check_password(password):
    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if 'A' <= ch <= 'Z':
            has_upper = True
        elif 'a' <= ch <= 'z':
            has_lower = True
        elif '0' <= ch <= '9':
            has_num = True
    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True
    return False


p = input('Введите пароль: ')
if check_password(p):
    print('Пароль надёжный')
else:
    print('Пароль не надёжный')
