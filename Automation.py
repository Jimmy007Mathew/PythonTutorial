import time
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.find_element(By.XPATH, '//*[@id="p-search"]/a').click()
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="searchform"]/div/div/div[1]/input').send_keys("Earth")
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="searchform"]/div/button').click()
time.sleep(5000)
# data=
# data.send_keys("hasan")
# time.sleep(5)