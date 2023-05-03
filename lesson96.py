class Power:
    '''
    Класс Power принимает свойство из декоратора Power и это свойство является число в которое будет возводиться
    результат полученный из функции func()
    '''

    def __init__(self, arg):
        self.arg = arg  # аргумент декоратора

    def __call__(self, fn):
        def wrap(*args, **kwargs):
            # print(self.arg)
            res = fn(*args, **kwargs)  # результат выражения функции func()
            # print(res)
            return f'Результат: {self.arg ** res}'

        return wrap


@Power(3)  # декоратор Power и аргумент принимающий декоратором, для возведения в степень
def func(a, b):  # декорируемая функция
    return a * b


print(func(a=2, b=2))
