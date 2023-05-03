import requests
from bs4 import BeautifulSoup
import re

url = requests.get('https://klops.ru')
soup = BeautifulSoup(url.text, 'html.parser')
soup1 = soup.findAll(class_='title')
soup2 = soup.findAll(class_='item')


klops_title = ''
klops_news = ''
lst = []
lst_href = []
i = 0
while i < 5:  # 35 all elements
    lst.append(soup1[i + 1].text)
    lst_href.append(soup2[i].get('href'))
    i += 1
lst_img = []
reg = r"[\w+]+://\d\.\w+\.\w+\.\w+/\w+/\w+\?*=*\?*\w+=*\w+"
for i in lst_href:
    url1 = requests.get(i)
    soup1 = BeautifulSoup(url1.text, 'html.parser')
    soup3 = soup1.findAll('link', {'itemprop': 'image'})
    res = re.findall(reg, str(soup3).strip(''))
    lst_img.append(res)

lst_image = []
lst_imagen = []
for i in range(len(lst_img)):
    lst_image.append(lst_img[i][0])
    lst_imagen.append(lst_image[i].replace("''", ' '))

print(lst_imagen)



# reg1 = r'[^\']+'
# lst_imagen = []
# for i in lst_image:
# res = re.findall(reg1, i)
# lst_imagen.append(i)
# print(lst_imagen)
