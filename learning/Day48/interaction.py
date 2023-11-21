from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# count=driver.find_element(By.CSS_SELECTOR,'#articlecount a')
# # count.click()

# link_text=driver.find_element(By.LINK_TEXT,"is elected")
# # link_text.click()

# search=driver.find_element(By.NAME,"search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)


# challenge
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname=driver.find_element(By.NAME,"fName")
fname.send_keys("ayush")

lname=driver.find_element(By.NAME,"lName")
lname.send_keys("neupane")

email=driver.find_element(By.NAME,"email")
email.send_keys("hello123@gmail.com")

email.send_keys(Keys.ENTER)

time.sleep(10)

