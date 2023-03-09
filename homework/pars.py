import requests
from bs4 import BeautifulSoup

url = requests.get('https://klops.ru')
soup = BeautifulSoup(url.text, 'html.parser')
soup1 = soup.findAll(class_='title')
soup2 = soup.findAll(class_='item')

klops_title = ''
klops_news = ''
lst = []
lst1 = []
i = 0
while i < 5:  # 35 all elements
    lst.append(soup1[i + 1].text)
    lst1.append(soup2[i].get('href'))
    i += 1
