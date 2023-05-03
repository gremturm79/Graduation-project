tpl = tuple(input('Введите элементы кортежа: '))
tpl1 = set(tpl)
print(tpl)
for i in tpl1:
    if i in tpl:
        print('Количество ', i, '=', tpl.count(i))
