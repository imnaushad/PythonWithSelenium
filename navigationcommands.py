from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://newtours.demouat.com/") #Flight Reservation application
time.sleep(5)
print(driver.title)

driver.get("http://pavantestingtools.blogspot.in") #Testing tools appli
time.sleep(5)
print(driver.title)

driver.back()
time.sleep(5)
print(driver.title)

driver.forward()
print(driver.title)




