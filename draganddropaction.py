from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source_element=driver.find_element("xpath", '//*[@id="box6"]')

target_element=driver.find_element("xpath", '//*[@id="box106"]')

actions=ActionChains(driver) #Object of actionchains class
actions.drag_and_drop(source_element,target_element).perform() #performs drag and drop action
