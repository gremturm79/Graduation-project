def funk_computer(a):
    def inner_funk(b):
        summa = b * a
        return summa
    return inner_funk


res = funk_computer(2)
print(res(15))
print(res(20))
res = funk_computer(3)
print(res(15))
print(res(20))
