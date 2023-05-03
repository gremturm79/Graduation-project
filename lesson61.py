import requests
import re

url = 'https://www.voicecards.ru/item/rozygryshi/zvonok_ot_znamenitosti/55955.html'

html_text = requests.get(url).text

reg = r'src="\w+://\w\.\w+\.\w+/\w/\d+\.mp3"'
url1 = re.findall(reg, html_text, flags=re.MULTILINE)
print(url1[0])
url2 = re.findall('(\")(.*)(\")', url1[0])
print(url2[0][1])
r = requests.get(url2[0][1])
str1 = 'music'
with open(str1 + '.mp3', 'wb') as f:
    f.write(r.content)


