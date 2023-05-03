# Посчитать количество элементов в списке

lst = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
count = 0  # Подсчёт количества вхождения во вложенные списки,
len_lst = 0  # Подсчёт количества элементов во вложенных списках
for i in range(len(lst)):
    if type(lst[i]) == list:
        count += 1
        len_lst += len(lst[i])
        for j in lst[i]:
            if type(j) == list:
                count += 1
                len_lst += len(j)
print(len_lst - count + len(lst))  # Количество элементов во вложенных списках вычитаем количество самих вложенных
# и прибавляем количество элементов самого списка


#  Вычислить количество отрицательных чисел при помощи рекурсии [-2, 3, 8, -11, -4, 6]   n = 3

cnt = 0  # переменная счётчик отрицательных элементов списка


def count_num(m):
    '''
    Функция выполняет подсчёт количества отрицательных элементов списка

    Функция принимает аргумент типа данных списка и возвращает количество отрицательных элементов списка,
    при помощи рекурсии.

    :param m: принимающий аргумент, тип данных список.
    :return: возвращает количество всех отрицательных элементов списка.
    '''
    global cnt
    if m == []:  # Базовое условие для выхода из рекурсии
        return cnt
    elif m[0] > 0:
        return count_num(m[1:])
    else:
        cnt += 1
        return count_num(m[1:])


lst_1 = [-2, 3, 8, -11, -4, 6]
print(count_num(lst_1))
