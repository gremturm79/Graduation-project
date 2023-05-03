from bs4 import BeautifulSoup
import re

# file1 = 'file10.txt'
# with open('Читать онлайн Доктора вызывали_ или Трудовые будни попаданки - Соня Марей.html', 'r', encoding='utf-8') as\
# file:
# test = file.read()
# with open(file1, 'w', encoding='utf-8') as f:
# file1 = f.write(test)
with open('file10.txt', 'r', encoding='utf-8') as f:
    file1 = f.read()
    reg = r'[А-я\.]+' # r'(\.</p><p>)([А-я]+)(\.</p><p>)'
    res = re.findall(reg, file1)
    res1 = ' '.join(res)
    print(res1)
    res2 = re.sub(r'\.\s', r'', res1)
    #res3 = re.sub(r'\s\s', r'', res2).strip('\n')
    print(res2)

    # for i in res:
    # print(i)
