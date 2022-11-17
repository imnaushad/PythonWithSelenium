from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(10)

driver.find_element("name", "username").send_keys("Admin")
driver.find_element("name", "password").send_keys("admin123")

driver.find_element("xpath", "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]").click()
#explicit wait lgana hai isme