import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    def test_Google(self):
        self.driver=webdriver.Chrome(executable_path=r"C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("The title of the page is:" +self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("The title of the page is:" + self.driver.title)
        self.driver.close()

if(__name__=="__main__"):
    unittest.main()