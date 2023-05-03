lst = [
    {'name': 'Jenifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nicolas', 'final': 98}
]
res = sorted(lst, key=lambda item: item['name'])
print(res)
res1 = sorted(lst, key=lambda item: item['final'], reverse=True)
print(res1)
