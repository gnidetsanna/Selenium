"""Test case to check the possibility to unsubscribe from course."""

import unittest

from selenium import webdriver
from pages import course_details_page as cdp
from pages import login_page as lp
from pages import profile_page as pp
from pages import courses_page as cp
from pages import base_page as bp


class UnsubscribeFromCourse(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = lp.LoginPage(self.driver)
        self.login_page.sign_in_as(**lp.VALID_DATA)
        self.login_page.is_page_loaded(bp.PROFILE_PAGE_URL)
        self.profile_page = pp.ProfilePage(self.driver)
        self.courses_page = cp.CoursesPage(self.driver)
        self.course_details_page = cdp.CourseDetailsPage(self.driver)
        self.courses_page.go_to()
        self.courses_page.click_on_first_course_on_page()

    def tearDown(self):
        self.course_details_page.unsubscribe_from_course()
        self.driver.close()

    def test_unsubscribe_from_course(self):
        """Test ability to unsubscribe from course."""
        self.course_details_page.click_on_subscribe_button()
        self.course_details_page.click_on_subscribe_button()
        self.assertTrue(self.course_details_page.message_unsubscribe_course())


if __name__ == "__main__":
    unittest.main(verbosity=2)




