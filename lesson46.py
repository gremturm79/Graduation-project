# работает только с предложениями где не менее трёх символов повторяющихся, меняет элемент.
str1 = input('Напишите строку: ')
# str1 = 'Замените в этой строке все появления буквы "о" на букву "О", кроме первого и последнего вхождения'

while True:
    s_old = input('Введите любую букву из строки: ')
    if str1.count(s_old) < 3:
        continue
    else:
        break
s_new = input(f'Введите любой букву (символ) на которую хотите поменять на букву _{s_old}_ * : ')

long = len(s_old)
a = str1.find(s_old)
b = str1.rfind(s_old)
str2 = str1[0:a] + str1[a:a + 1]
str3 = str1[a + 1:b]
str3 = str3.replace(s_old, s_new)
str4 = str1[b:]
str5 = str2 + str3 + str4
print(str5)
