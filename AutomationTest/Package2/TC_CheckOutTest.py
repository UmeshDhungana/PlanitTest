import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from TC_ShopTest import ShopTest

class CheckOutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/Users/Umesh/Desktop/geckodriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        self.base_url = 'https://jupiter.cloud.planittesting.com'

    def test_DeliveryDetails(self):
        print("Checking Delivery Details of User: ")

        driver = self.driver
        driver. get(self.base_url)

        fname = 'umesh'
        sname = 'dhungana'
        user_email = 'dum77ss@gmail.com'
        address = '110/120 Dora Street, Hurstville'

        card_type = 'Visa'
        card_num = 32453243532

        # clicking shop button
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/p[2]/a').click()

        # selecting toys
        toy1 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/ul/li[1]/div/p/a')
        toy1.click()
        toy1.click()

        #clicking cart at top right
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/ul[2]/li[4]/a/span').click()

        #clicking check out button
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/form/table/tfoot/tr[2]/td/a').click()

        self.driver.find_element(By.ID, 'forename').send_keys(fname)
        self.driver.find_element(By.ID, 'surname').send_keys(sname)
        self.driver.find_element(By.ID, 'email').send_keys(user_email)
        self.driver.find_element(By.ID, 'address').send_keys(address)

        select = Select(self.driver.find_element(By.ID, 'cardType'))
        select.select_by_value(card_type)

        self.driver.find_element(By.ID, 'card').send_keys(card_num)

        self.driver.find_element(By.ID, 'checkout-submit-btn').click()

        # self.assertIn("", "")
        self.assertNotIn(" Almost there - but we can't send your items unless you complete the form correctly. ",
                         self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div').text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()