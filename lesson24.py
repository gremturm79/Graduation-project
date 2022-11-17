dict_sale = {
    'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
    'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
    'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
    'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451},
}
for name in dict_sale:
    print(' ', name)
    for j in dict_sale[name]:
        print(j, ':', dict_sale[name][j])
while True:
    name1 = input('Введите имя: ')
    if name1 in dict_sale:
        break
    else:
        print('Повторить поиск')
while True:
    region = input('Ведите регион: ')
    if region in dict_sale[name1]:
        break
    else:
        print('Повторить поиск')


print('Имя: ', name1)
print('Регион: ', region)
print('Значение объёма продаж: ', dict_sale[name1][region])
val = int(input('Новое значение: '))
dict_sale[name1][region] = val
print(dict_sale[name1])

