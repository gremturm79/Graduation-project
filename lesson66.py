text1 = 'text1.txt'
# создаём файл text1 и записываем в него текст
with open(text1, 'w', encoding='utf-8') as f:
    text1 = f.write('Строка 1\nСтрока 2\nСтрока 3\nСтрока 4\nСтрока 5\nСтрока 6\nСтрока 7\nСтрока 8\n')

text2 = 'text2.txt'
# создаём файл text2 и записываем в него текст
with open(text2, 'w', encoding='utf-8') as f2:
    text2 = f2.write('Линия 1\nЛиния 2\nЛиния 3\nЛиния 4\nЛиния 5\nЛиния 6\nЛиния 7\nЛиния 8\n')
# открываем файлы text1 и text2 и создаём text3
text3 = 'text3.txt'
with open('text1.txt', 'r', encoding='utf-8') as f1, open('text2.txt', 'r', encoding='utf-8') as f2, open(text3, 'w', \
                                                                                                          encoding='utf-8') as fw:
    lst1 = f1.readlines()  # используем readlines для создания списка из строк текста
    lst2 = f2.readlines()
    lst3 = []
    for i in lst1:
        i = i[:-1]  # удаляем элемент табуляции
        lst3.append(i)  # записываем элементы в список
    for lines in range(len(lst1)):
        fw.write(lst3[lines] + '. ' + lst2[lines])  # записываем строки в файл text3.txt