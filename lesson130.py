import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.gubernia.com/projects/news/'
req = requests.get(url)

soup = BeautifulSoup(req.text, 'html.parser')
soup1 = soup.findAll('div', class_='news-name')
soup2 = soup.findAll('a', class_="news-box")
lst = []
lst_href = []
k = 0
c = 0
for i in soup1:
    if k < 5:
        lst.append(i.text)
        k += 1
for i in soup2:
    if c < 5:
        lst_href.append(i.get('href'))
        c += 1


print(lst)
print(lst_href)

