import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By



class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/Users/Umesh/Desktop/geckodriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        self.base_url = 'https://jupiter.cloud.planittesting.com'

    #Invalid User Check
    def test_LoginByUsername(self):
        print("Login By Username test: ")
        driver = self.driver
        driver.get(self.base_url)

        self.driver.find_element(By.ID,"nav-login").click()
        self.driver.find_element(By.ID,"loginUserName").send_keys("umesh")
        self.driver.find_element(By.ID,"loginPassword").send_keys("1234567")
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/button[1]").click()
        self.driver.implicitly_wait(2)
        expected_text = "Your login details are incorrect"
        actual_text = self.driver.find_element(By.XPATH,'//*[@id="login-error"]').text

        assert expected_text == actual_text, f'Error: Invalid User has Access'



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()