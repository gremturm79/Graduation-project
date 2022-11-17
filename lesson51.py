import re

date = input('Введите дату в формате dd-mm-YYYY :  ')

reg = r'([12][0-9]|[3][01])-([0][1-9]|[1][12])-([12][09][0-9][0-9])'
print(re.findall(reg, date))

telefone = input('Введите номер телефона: ')
reg = r'[+][7][0-9]{10}|[+]?[7][\s][(]?[0-9]{3}[)]?\s[0-9]{3}[\s|-][0-9]{2}[\s|-][0-9]{2}'


print(re.findall(reg, telefone))