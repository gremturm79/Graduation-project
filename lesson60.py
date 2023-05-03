# Обменять местами две строки в файле

f = open('text5.txt', 'w') # создаём файл в режими записи текста
f.write('Hello World\nMy name John\nI live New York\n') # записываем в файл строку
f.close()
fr = open('text5.txt', 'r+') # открываем файл для чтения и записи
readline = fr.readlines() # получаем список строк файла fr
print(readline)
a = int(input('Введите строку 1: ')) # создаём пременные для использования их как индексы списка readlines
b = int(input('Введите строку 2: '))

if 0 <= a < len(readline) and 0 <= b < len(readline) : # проверка правильности ввода переменных a и b
    # чтобы не выйти за диапазон длины списка
    readline[a], readline[b] = readline[b], readline[a] # меняем местами элементы списка по их индексу
    print(readline)
else:
    print('Текст не имеет введённое количество строк')
fr.close()

f = open('text5.txt', 'w')
f.writelines(readline) # записываем последовательность списка readline в файл f
f.close() # закрываем файл
