"""Test case for blackbox testing of the
possibility to view a course details page."""

import unittest
from selenium import webdriver
from pages import course_details_page as cdp
from pages import courses_page as cp


class CourseDetails(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.courses_page = cp.CoursesPage(self.driver)
        self.course_details_page = cdp.CourseDetailsPage(self.driver)
        self.courses_page.go_to()

    def tearDown(self):
        self.driver.close()

    def test_course_details_are_present(self):
        """Test to check presence of all course attributes on page."""
        self.course_details_page.find_course()
        self.course_details_page.click_on_course()
        self.assertTrue(self.course_details_page.is_all_attributes_of_course_present())


if __name__ == "__main__":
    unittest.main()
