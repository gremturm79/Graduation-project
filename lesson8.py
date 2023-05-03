lst = [int(input('->')) for i in range(int(input('Введите количество элементов:  ')))]
k = int(input('Введите индекс: '))
print('k =', k)
c = int(input('Введите значение: '))
print('c =', c)
lst.insert(k, c)
print(lst)
