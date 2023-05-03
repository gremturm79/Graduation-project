size = 8
m = (2 * size) - 2
for i in range(size):
    for j in range(m):
        print(end=' ')
    m = m - 1
    for j in range(0, i + 1):
        print('*', end=' ')
    print(' ')
print(f'С новым годом!!!'.upper().center(30, '*'))
