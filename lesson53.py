from functools import wraps


def add_autor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        autor = 'Jong Jou'
        return autor + '\n' + func(*args, **kwargs)

    return wrapper


@add_autor
def get_title(title):
    '''
     A func a receiver and return
    '''
    return title


print(get_title.__name__)
print(get_title.__doc__)
