import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#log into the admin and remove a category
class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "testuser@mail.com"
        pwd = "test123"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin/")
        time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/admin/store/category/")
        time.sleep(3)
        driver.get("http://127.0.0.1:8000/admin/store/category/1/change")
        #assert "Logged in"
        time.sleep(3)
        driver.get("http://127.0.0.1:8000/admin/store/category/1/delete")
        try:
            # attempt to find the 'Logout' button - if found, logged in
           elem = driver.find_element_by_xpath("//*[@id='content']/form/div/input[2]").click()



           assert True

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()