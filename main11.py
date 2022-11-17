def func(arg):
    def wrapper(fn):
        midl = 1

        def wrap(*args):
            nonlocal midl
            fn(*args)
            print('Сумма чисел', ', '.join(map(str, args)), '=', fn(*args))
            midl = round(sum(args) / len(args), 1)
            return 'Среднее арифметическое чисел ' + ', '.join(map(str, args)) + ' = ' + str(midl)

        return wrap

    return wrapper


@func('Среднее арифметическое чисел')
def mult(*args):
    return sum(args)


print(mult(2, 2, 3))
print(mult(2, 42, 56, 78))
print(mult(45, 12, 58, 23))
