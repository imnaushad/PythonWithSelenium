from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in/")
driver.maximize_window()

#driver.save_screenshot(r"D:\Naushad\screenshot.png")

driver.get_screenshot_as_file(r"D:\Naushad\ss1.png")