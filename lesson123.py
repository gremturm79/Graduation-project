from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
options = Options()
options.add_argument("window-size=1400,600")


ua = UserAgent()
user_agent = ua.random
print(user_agent)
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://whoer.net/')
driver.quit()
