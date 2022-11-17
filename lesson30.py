def res(*args):
    d = 0
    for i in range(len(args)):
        d = d + args[i]
        print(d, end=' ')
    print()


res(3, 9, 1)
res(2, 5, 4, 2)
res(3, 5, 10, 6, 3)
