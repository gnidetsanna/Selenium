"""test case to check the possibility to logout from the system"""

import unittest
from selenium import webdriver
from pages import login_page as lp
import time

class logout_test(unittest.TestCase):
    """check the possibility to logout from the system"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = lp.LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_logout_user(self):
        self.login_page.sign_in_as(**lp.VALID_DATA)
        self.login_page.sign_out()
        self.assertTrue(
            self.login_page.is_sign_up_button_present())

    def test_logout_trainer(self):
        self.login_page.sign_in_as(**lp.TRAINER_DATA)
        self.login_page.sign_out()
        self.assertTrue(
            self.login_page.is_sign_up_button_present())

    def test_logout_moderator(self):
        self.login_page.sign_in_as(**lp.MODERATOR_DATA)
        self.login_page.sign_out()
        self.assertTrue(
            self.login_page.is_sign_up_button_present())

    def test_logout_admin(self):
        self.login_page.sign_in_as(**lp.ADMIN_DATA)
        self.login_page.sign_out()
        self.assertTrue(
            self.login_page.is_sign_up_button_present())

if __name__ == "__main__":
    unittest.main(verbosity=2)
