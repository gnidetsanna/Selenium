"""Test cases for Black Box testing of Possibility
for user to enter the system"""

import unittest
from selenium import webdriver
from pages import login_page as lp
from pages import profile_page as pp
from pages import base_page


class UsersSignIn(unittest.TestCase):
    """Login as different user's to test possibility
    to enter the system with different roles
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.login_page = lp.LoginPage(self.driver)
        self.profile_page = pp.ProfilePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_user(self):
        """method to test login as common user"""
        self.login_page.sign_in_as(**lp.VALID_DATA)
        self.assertTrue(
            self.login_page.is_page_loaded(base_page.PROFILE_PAGE_URL))

    def test_login_admin(self):
        """method to test login as admin user"""
        self.login_page.sign_in_as(**lp.ADMIN_DATA)
        self.assertTrue(
            self.login_page.is_page_loaded(base_page.PROFILE_PAGE_URL))

    def test_login_moderator(self):
        """method to test login as moderator"""
        self.login_page.sign_in_as(**lp.MODERATOR_DATA)
        self.assertTrue(
            self.login_page.is_page_loaded(base_page.PROFILE_PAGE_URL))

    def test_login_trainer(self):
        """method to test login as trainer"""
        self.login_page.sign_in_as(**lp.TRAINER_DATA)
        self.assertTrue(
            self.login_page.is_page_loaded(base_page.PROFILE_PAGE_URL))

if __name__ == "__main__":
    unittest.main(verbosity=2)
