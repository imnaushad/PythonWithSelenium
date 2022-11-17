from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(5)
driver.execute_script("arguments[0].scrollIntoView();", driver.find_element("id", 'RESULT_FileUpload-10'))
driver.find_element("id", 'RESULT_FileUpload-10').send_keys(r"D:/Naushad/AXA Project/axa_project.txt")




