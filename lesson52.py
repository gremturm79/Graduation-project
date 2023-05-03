import re

telefone = input('Введите номер телефона : ')
reg = r'[+][7][0-9]{10}|[+]?[7][\s][(]?[0-9]{3}[)]?\s[0-9]{3}[\s|-][0-9]{2}[\s|-][0-9]{2}'


print(re.findall(reg, telefone))


