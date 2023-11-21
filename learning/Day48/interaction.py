from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

count=driver.find_element(By.CSS_SELECTOR,'#articlecount a')

print(count.text)