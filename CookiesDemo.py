from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in/")
driver.maximize_window()

#Capture all the cookies created by browser

cookies=driver.get_cookie()
print(len(cookies))   #no. of cookies being created
print(cookies)  #print all the cookie pairs

#Adding new cookie to the browser
cookie=('name':'Mycookie','value':'1234567890')
driver.add_cookie(cookie)    #add cookie to the browser

cookies=driver.get_cookie()
print(len(cookies))   #no. of cookies being created
print(cookies)  #print all the cookie pairs

#Deleting the cookie
driver.delete_cookie('Mycookie')

cookies=driver.get_cookie()
print(len(cookies))   #no. of cookies being created
print(cookies)  #print all the cookie pairs

#deleting all the cookies
driver.delete_all_cookies()
cookies=driver.get(cookies)
print(len(cookies))



