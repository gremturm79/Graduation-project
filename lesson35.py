def func(a, b, c):
    def paralel_sqr():
        s = 2 * (a * b + b * c + a * c)
        return s

    def arctangel_sqr():
        s = a * b
        return s

    def start():
        pass

    start.paralel_sqr = paralel_sqr
    start.arctangel_sqr = arctangel_sqr
    return start


res = func(2, 2, 2)
print(res.paralel_sqr())
print(res.arctangel_sqr())
