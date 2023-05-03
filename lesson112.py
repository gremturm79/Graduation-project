from bs4 import BeautifulSoup
import re


# def copywriter(tag):
# whois = tag.find('div', class_='whois').text.strip()
# if 'Copywriter' in whois:
# return tag
# return None

def get_salary(s):
    reg = r'\d+'
    res = re.findall(reg, s)[0]
    print(res)


f = open('index.html', 'r', encoding='utf-8').read()
soup = BeautifulSoup(f, parser='html', features='lxml')
row = soup.find_all('div', {'data-set': 'salary'})
for i in row:
    get_salary(i.text)

# copywriters = []

# for i in row:
# cw = copywriter(i)
# if cw:
# copywriters.append(cw)

# print(copywriters)
# row = soup.find_all('div', class_='name')
# for i in row:
# print(i.text)
