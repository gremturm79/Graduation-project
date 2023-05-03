lst = [int(input('->')) for i in range(int(input('Введите количество элементов')))]
print(lst)
ch = int(input('Введите число: '))
for i in range(len(lst)):
    if lst[i] == ch:
        print(ch)


