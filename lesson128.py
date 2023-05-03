from bs4 import BeautifulSoup
import requests
import re

res = r'^[//+\w+\.+\w+//+\w+.jpeg]$'
url = requests.get('https://www.kinomania.ru/news')
soup = BeautifulSoup(url.content, 'html.parser')
t = soup.findAll(class_='pagelist-item-title')
for i in t:
    print(i.text)
image = soup.findAll('img')
lst = []
for i in image:
    lst.append(i['src'])

reg = r'[//f+\w+\.+jpeg]'
lst1 = []
for i in lst:
    res = re.findall(reg, i)
    if len(res) < 26:
        continue
    lst1.append('https:' + ''.join(res))

print(lst1)
