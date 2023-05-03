import re

str1 = '1x, Text ABC 123 A1B2C3'  # Найти цифры, рядом с которой нет цифры    ['1', '1', '2', '3']
str2 = 'text from #START# till #END#'  # Найти текст от #START# до #END#     ['till']
str3 = '12_34__56'  # Найти последовательность цифр, после которой идёт ровно одно подчёркивание ['12']

reg1 = r'(?<!\d)\d(?!\d)'
print(re.findall(reg1, str1))

reg2 = r'(?:\#\s)(\w+)(?:\s\#)'
print(re.findall(reg2, str2))

reg3 = r'\d+(?=_(?!_))'
print(re.findall(reg3, str3))

