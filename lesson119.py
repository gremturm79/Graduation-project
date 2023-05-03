from selenium import webdriver
import time
from fake_useragent import UserAgent
from random import *
from selenium.webdriver.common.by import By

url = r'https://bookriver.ru/reader/sonya-marey-doktora-vyzyvali-ili-trudovye-budni-popadanki/448929'
url1 = r'https://www.whatismybrowser.com/'
useragent = UserAgent()
useragent1 = useragent.browsers()
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={useragent}')
EXE_PATH = r'C:\Users\Alex\chromedriver.exe'  # EXE_PATH это путь до ранее загруженного нами файла chromedriver.exe
driver = webdriver.Chrome(executable_path=EXE_PATH, options=options)  # запуск Chrome

try:
    driver.get(url=url1)
    time.sleep(5)
    #driver.save_screenshot('i.png')
except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()







# print(driver.page_source)  HTML код всего содержимого нашей страницы class s1p86qy6_SCContent
