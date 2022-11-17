from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="")
driver.get("http://demo.automationtesting.in/Window.html")
print(driver.title)

print(driver.current_url)

driver.find_element_by_xpath("")

time.sleep(5)

#driver.close()
driver.quit()
