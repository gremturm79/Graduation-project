def wrapper(fn):
    def wrap(*args):
        print('Среднеарифметическое чисел', str(args), '=', round(fn(*args) / len(args), 2))

    return wrap


@wrapper
def mult(*args):
    print('Сумма чисел', ', '.join(map(str, args)), '=', sum(args))
    return sum(args)


mult(2, 2, 3)
mult(2, 42, 56, 78)
mult(45, 12, 58, 23)
