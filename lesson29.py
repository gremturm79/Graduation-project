def calc(*args):
    calculate = 1
    for i in args:
        calculate *= i
    return print(calculate)


calc(10, 9)
calc(2, 3, 4)
calc(3, 5, 10, 6)
