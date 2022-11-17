str1 = input('Введите строку : ')
print(str1)
s_ch = input('Заменяемая подстрока : ')
print(s_ch)
s_new = input('Новая подстрока : ')
print(str1.find(s_ch))
a = str1.find(s_ch)
b = str1.find(s_ch, a + 1)
c = 0
str4 = ''
for i in str1:
    if s_ch in str1:
        str4 += str1.replace(s_ch, s_new)
    break

print(f'Изменённая строка : {str4}')
