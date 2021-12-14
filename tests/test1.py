import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#login as a user and logout
class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "dustin@mail.com"
        pwd = "play2win"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/")
        driver.get("http://127.0.0.1:8000/account/login")
        elem = driver.find_element_by_id("login-username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("login-pwd")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        #assert "Logged in"
        try:
            # attempt to find the 'Logout' button - if found, logged in
           elem = driver.find_element_by_xpath("/html/body/header/nav/div/div[1]/a[2]/div")

           assert True

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
