import requests
from bs4 import BeautifulSoup

url = requests.get('https://kinogo-official.ru/filmy/')
soup = BeautifulSoup(url.content, 'html.parser')

soup1 = soup.findAll('h2')
soup2 = soup.findAll('a', class_='kino-h')
soup5 = soup.findAll('div', class_='kinopoisk')
soup6 = soup.findAll('div', class_='kino-img img-box')
a = 0
for el in range(len(soup1)):
    i = 0
    soup3 = soup1[el].text
    soup4 = soup2[el].get('href')
    t = soup5[el].findAll('span')
    t1 = soup6[el].findNext('img').get('src')
    print(soup3)
    print(t1)
    print(soup4)
    print(t[0].text)
    print(t[1].text)

# for el in range(len(soup2)):
# soup4 = soup2[el].get('href')
# print(soup4)

#for el in range(len(soup5)):
   # i = soup5[el].select('span')
    #for j in range(len(i)):
       # print(i[j].text)
