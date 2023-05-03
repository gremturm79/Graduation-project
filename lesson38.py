
lst = [
    {'name': 'Jenifer', 'final': 99},
    {'name': 'David', 'final': 97},
    {'name': 'Nicolas', 'final': 98}
]
print(lst)
print()

res2 = list(sorted(lst, key=lambda x: x['final']))

print('Максимальная оценка', res2[-1])
print('Минимальная оценка', res2[0])

print()
print()


def check(a):
    for i in range(len(res)):
        if res[i] == min(res):
            print('Минимальная оценка', lst[i])
        if res[i] == max(res):
            print('Максимальная оценка', lst[i])


res = list(map(lambda x: x['final'], lst))
check(res)




