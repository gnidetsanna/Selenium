"""test case to check view courses list"""
import unittest
from selenium import webdriver
from pages import courses_page as cp
from pages import login_page as lp
import time


class view_courses_list(unittest.TestCase):
    """check view courses list"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.courses_page = cp.CoursesPage(self.driver)
        self.login_page = lp.LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_view_courses_list_as_unautorized_user(self):
        """test to verify possibility to view the list of courses as
        unautorized user"""
        self.courses_page.go_to()
        self.assertTrue(self.courses_page.is_courses_on_page())

    def test_view_courses_list_as_user(self):
        """test to verify possibility to view the list of courses as user"""
        self.login_page.sign_in_as(**lp.VALID_DATA)
        self.courses_page.go_to()
        self.assertTrue(self.courses_page.is_courses_on_page())

    def test_view_courses_list_as_trainer(self):
        """test to verify possibility to view the list of courses as trainer"""
        self.login_page.sign_in_as(**lp.TRAINER_DATA)
        self.courses_page.go_to()
        self.assertTrue(self.courses_page.is_courses_on_page())

    def test_view_courses_list_as_moderator(self):
        """test to verify possibility to view the list of courses as trainer"""
        self.login_page.sign_in_as(**lp.MODERATOR_DATA)
        self.courses_page.go_to()
        self.assertTrue(self.courses_page.is_courses_on_page())

    def test_view_courses_list_as_admin(self):
        """test to verify possibility to view the list of courses as trainer"""
        self.login_page.sign_in_as(**lp.ADMIN_DATA)
        self.courses_page.go_to()
        self.assertTrue(self.courses_page.is_courses_on_page())


if __name__ == "__main__":
    unittest.main(verbosity=2)
