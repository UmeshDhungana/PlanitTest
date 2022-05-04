import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class ShopTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/Users/Umesh/Desktop/geckodriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        self.base_url = 'https://jupiter.cloud.planittesting.com'

    def test_Buy(self):
        print("Checking Buy: ")

        driver = self.driver
        driver.get(self.base_url)

       #clicking shop button
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/p[2]/a').click()

        #selecting toys
        toy1 = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/ul/li[1]/div/p/a')
        toy1.click()
        toy1.click()

        self.assertIn('2',self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/ul[2]/li[4]/a/span').text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()