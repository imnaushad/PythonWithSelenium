import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        #driver = None                 #returns true
        #self.assertIsNone(driver)     #it verifies whether the driver object contains any values or not
        self.assertIsNotNone(driver)   #returns true


if __name__ == "__main__":
    unittest.main()
