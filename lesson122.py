from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import random

URL = 'https://lo18.lordfilm.lu/filmy/zarubezhnye-f/'
ua = UserAgent()
a = ua.random
options = Options()
options.add_argument("window-size=1400,600")
ua = UserAgent()
user_agent = ua.random
options.add_argument(f'user-agent={user_agent}')
# options = webdriver.ChromeOptions()
# options.headless = True

driver = webdriver.Chrome(chrome_options=options)
driver.get(URL)
time.sleep(8)
S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
driver.find_element(By.TAG_NAME, 'body').screenshot('klops1.png')
checkbox = driver.find_element(By.TAG_NAME, 'button')
checkbox.click()
time.sleep(5)
S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
driver.find_element(By.TAG_NAME, 'body').screenshot('klops2.png')
driver.quit()