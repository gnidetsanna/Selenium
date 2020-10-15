"""Test case to check th possibility to
leave the comment to course.
"""

import unittest

from selenium import webdriver
from pages import course_details_page as cdp
from pages import login_page as lp
from pages import profile_page as pp
from pages import courses_page as cp
from pages import base_page as bp


class LeaveCommentToCourse(unittest.TestCase):
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
        self.driver.close()

    def test_possibility_to_leave_comment(self):
        """Test ability to leave comment to course."""
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        self.course_details_page.write_a_comment()
        self.course_details_page.click_on_comment_button()
        self.driver.refresh()
        self.assertTrue(self.course_details_page.find_comment())


if __name__ == "__main__":
    unittest.main()
