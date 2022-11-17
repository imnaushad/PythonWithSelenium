#assertIn & assertNotIn

import unittest

class Test(unittest.TestCase):
    def testName(self):
        list={"python", "Selenium", "Java"}

        #self.assertIn("python",list)    #returns true
        #self.assertIn("ruby",list)    #returns false or gets failed

#assertNotIn

        #self.assertNotIn("ruby", list)  #passed, returns true
        self.assertNotIn("python", list)  #failed, returns false

if __name__ == "__main__":
    unittest.main()
