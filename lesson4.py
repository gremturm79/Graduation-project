try:
    i = int(input('Введите число: '))
    b = int(input('Введите число: '))
    A = i
    B = b
    res = 0
    if i < b:

        while i <= b:
            if i % 2 != 0:
                res += i
            i += 1
        print('Результат', res)
    else:

        while b <= i:
            if b % 2 != 0:
                res += b
            b += 1
        print('Результат', res)
except ValueError:
    print('Что-то пошло не так')

else:
    print('Сумма всех целых нечётных чисел в диапазоне от', A, ' до', B, 'равна:', res)

finally:
    print('Программа завершена')
