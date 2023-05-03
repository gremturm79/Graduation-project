a = [int(input('-> ')) for i in range(int(input('Введите количество элементов: ')))]
lst = []
lst_2 = []
b = 0
for i in range(len(a)):
    lst.extend([a[i]])
    if a[i] > 0:
        lst_2.extend([a[i]])
for i in range(len(lst_2)):
    if lst_2[i] > b:
        b = lst_2[i]
print('Список:  ', lst)
print('Новый список состоящий из положительных элементов: ', lst_2)
print('Наибольший элемент из списка: ', b)
