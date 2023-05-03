import requests
from bs4 import BeautifulSoup

url = requests.get('https://klops.ru')
soup = BeautifulSoup(url.text, 'html.parser')
soup1 = soup.findAll(class_='title')
soup2 = soup.findAll(class_='item')

klops_title = ''
klops_news = ''
lst = []
lst_link = []
i = 0
while i < 5:  # 35 all elements

    lst.append(soup1[i + 1].text)
    lst_link.append(soup2[i].get('href'))
    i += 1
print(lst)
lst_text = []
for i in lst_link:
    url1 = requests.get(i)
    soup = BeautifulSoup(str(url1), 'html.parser')
    soup1 = soup.find_previous_siblings('div')
    lst_text.append(soup1)

print(lst_text)
#lst1 = []
#for i in lst:
    #if i % 2 != 0:
        #lst1.append(i)
        #del lst[i]
