from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.python.org/")

event_list=driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul')

event_name=event_list.find_elements(By.CSS_SELECTOR,"a")
event_time=event_list.find_elements(By.TAG_NAME,"time")

events_name_lists=[t.text for t in event_name]
events_time_lists=[t.text for t in event_time]



events={}

for n in range(len(event_time)):
	events[n]={
	"name":events_name_lists[n],
	"time":events_time_lists[n]
	}
	

print(events)



