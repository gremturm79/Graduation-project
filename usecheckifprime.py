def typed(*args, **kwargs):
    def wrapper(fn):
        def wrap(*f_args, **f_kwargs):
            for i in range(len(args)):
                if type(f_args[i]) != args[i]:
                    raise TypeError('Некорректный тип данных')
                for k in kwargs:
                    if type(f_kwargs[k]) != kwargs[k]:
                        raise TypeError('Некорректный тип данных')
            return fn(*f_args, **f_kwargs)

        return wrap

    return wrapper


@typed(int, int, int)
def typed_fn(a, b, c):
    return a * b * c


@typed(str, str, str)
def typed_fn2(a, b, c):
    return a + b + c


@typed(str, str, c=int)
def typed_fn3(a, b, c='Hello'):
    return (a + b) * c


print(typed_fn(3, 4, 5))
# print(typed_fn(3, 4, 'Doge'))
print(typed_fn2('Hello', 'World', '!'))
print(typed_fn3('Hello', 'World  ', c=5))
