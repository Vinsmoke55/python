from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.python.org/")

logo=driver.find_element(By.CLASS_NAME,"python-logo")

documentation_link=driver.find_element(By.CSS_SELECTOR,".documentation-widget a")

bug=driver.find_element(By.XPATH,'//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

print(logo.get_attribute("src"))

print(logo.size)

print(documentation_link.text)

print(bug.text)