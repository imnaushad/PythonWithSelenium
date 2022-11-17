import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

        driver.get("https://www.google.com/")
        titleOfWebpage= driver.title

        #self.assertTrue(titleOfWebpage == 'Google')   #True
        self.assertFalse(titleOfWebpage == 'Google123') #returns True
if __name__ == "__main__":
    unittest.main()
