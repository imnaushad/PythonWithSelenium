from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chromeOptions=Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory": r"D:\Naushad\AXA Project"})

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe", chrome_options=chromeOptions)

driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

#Download the text file

driver.find_element(By.ID, 'textbox').send_keys("testng download file func")
driver.find_element(By.ID, 'createTxt').click() #generate button click
driver.find_element(By.ID, 'link-to-download').click() #download button click

#Download pdf file

driver.find_element(By.ID, 'pdfbox').send_keys("hello, i am wirtingasdfds")
driver.find_element(By.ID, 'createPdf').click() #generate button click
driver.find_element(By.ID, 'pdf-link-to-download').click() #download button click

driver.close(5)


