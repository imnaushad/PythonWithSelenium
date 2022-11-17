from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

inputboxes=driver.find_elements(By.CLASS_NAME, 'text_field')

print(len(inputboxes))

driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("Naushad")
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys("Alam")

driver.find_element(By.ID, 'RESULT_TextField-3').send_keys("8585978036")
driver.find_element(By.ID, 'RESULT_TextField-4').send_keys("INDIA")
driver.find_element(By.ID, 'RESULT_TextField-5').send_keys("NEW DELHI")
driver.find_element(By.ID, 'RESULT_TextField-6').send_keys("naushad@gmail.com")


