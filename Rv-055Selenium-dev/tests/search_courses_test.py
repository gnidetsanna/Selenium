"""test case to check course search"""
import unittest
from selenium import webdriver
from pages import courses_page as cp
import time


class search_field_disappears_after_second_click(unittest.TestCase):
    """check course search"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.courses_page = cp.CoursesPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_search_field_disappears_after_second_click(self):
        """test to check search field disappears after second click"""
        self.courses_page.go_to()
        self.courses_page.click_on_search_icon()
        self.courses_page.second_click_on_search_icon()
        self.assertFalse(self.courses_page.is_search_fild_active())

if __name__ == "__main__":
    unittest.main(verbosity=2)
