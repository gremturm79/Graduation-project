import re

str1 = 'Замените в этой строке все появления буквы "о" на букву "О", кроме первого и последнего вхождения.'
print(str1)
print(type(str1))
str1 = str1.split()
print(str1)

for i in range(len(str1)):
    a = str1[i].find('о')
    b = str1[i].rfind('о')
    str1[i] = str1[i].replace('о', 'О')
    print(str1[i], end=' ')
