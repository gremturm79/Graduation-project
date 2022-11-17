a = 5
b = 7
c = 3
sum = a + b + c
mult = a * b * c
aritm_mean = sum/3
print('Сумма:', sum)
print('Произведение:', mult)
print('Среднее арифметическое:', aritm_mean)

e = 1
d = 2
print(id(e))
print(id(d))
e = e + d
d = e - d
e = e - d
print(id(e))
print(id(d))
