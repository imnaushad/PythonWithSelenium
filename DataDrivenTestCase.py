from selenium import webdriver
from selenium.webdriver.common.by import By
import XLUtils

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://newtours.demouat.com/")
driver.maximize_window()

path=r"D:\Naushad\Login1.xlsx"

rows=XLUtils.getRowCount(path,'Sheet1')

for r in range(2, rows+1):
    username=XLUtils.readData(path, "Sheet1", r, 1)
    password=XLUtils.readData(path, "Sheet1", r, 2)

    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)

    driver.find_element("name", "login").click()

    if driver.title=="":   #copy title after login by inpect
        print("test is passed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test passed")
    else:
        print("test is failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test failed")

driver.find_by_link_text("Home").click()




