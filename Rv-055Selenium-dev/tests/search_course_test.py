"""Test case for the possibility to search a course"""

import unittest
from os import name

from selenium import webdriver
from pages import courses_page as cp
from pages import base_page as bp
from locators.courses_locators import CoursesPageLocators as cpl


class SearchCourse(unittest.TestCase):
    """Open the courses page to have a possibility to perform a search"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.courses_page = cp.CoursesPage(self.driver)
        self.courses_page.go_to()
        self.base_page = bp.BasePage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_perform_course_search(self):
        """Test for the ability to perform search of the particular course."""
        self.courses_page.find_search_icon_by_css(cpl.SEARCH_ICON)
        self.courses_page.click_on_search_icon()
        self.base_page.fill_in_text_field_by_css(cpl.SEARCH_ICON, 'trekking')
        self.courses_page.click_on_search_icon()
        self.assertTrue(self.courses_page.is_valid_text_on_page())


if __name__ == "__main__":
    unittest.main(verbosity=2)
