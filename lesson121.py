from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = 'https://lo18.lordfilm.lu/filmy/zarubezhnye-f/'

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get(URL)
time.sleep(5)
S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
driver.find_element(By.TAG_NAME, 'body').screenshot('web_screenshot1.png')
checkbox = driver.find_element(By.LINK_TEXT, 'Загрузить ещё')
checkbox.click()
time.sleep(5)
S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
driver.find_element(By.TAG_NAME, 'body').screenshot('web_screenshot2.png')
driver.quit()
