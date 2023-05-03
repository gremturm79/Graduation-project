import time

from selenium import webdriver
from selenium.webdriver.common.by import By
url = r'https://bookriver.ru/reader/sonya-marey-doktora-vyzyvali-ili-trudovye-budni-popadanki/448929'
EXE_PATH = r'C:\Users\Alex\chromedriver.exe'
driver = webdriver.Chrome(executable_path=EXE_PATH)
driver.get(url)
time.sleep(5)
# el = driver.find_element(By.TAG_NAME, 'body').screenshot('it.png')
el = driver.find_element_by_tag_name('body')
el.screenshot(path)
driver.quit()
