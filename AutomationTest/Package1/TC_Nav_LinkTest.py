import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Nav_LinkTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/Users/Umesh/Desktop/geckodriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        self.base_url = 'https://jupiter.cloud.planittesting.com/#/shop'



    def test_HomeLink(self):
        print("Test Home Link:  ")
        driver = self.driver
        driver.get(self.base_url)

        self.driver.find_element(By.ID,"nav-home").click()

        actual_text = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/h1').text
        expected_text = "Jupiter Toys"
        self.assertTrue(actual_text,expected_text)

    """
    Similar test cases can be created for all the navigation links
    """

    # def test_ContactLink(self):
    #     print("Test Contact Link:  ")
    #     self.assertTrue(True)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()