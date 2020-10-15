import unittest
from selenium import webdriver
from pages import login_page as lp
from pages import courses_page as cp
from pages import profile_page as pp
from helpers.create_and_delete_course import testCourse




class CourseTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.test_course = testCourse()
        cls.test_course.create_test_course()

    @classmethod
    def tearDownClass(cls):

        cls.test_course = testCourse()
        cls.test_course.delete_test_course()
        cls.test_course.close_connection()

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.login_page = lp.LoginPage(self.driver)
        self.profile_page = pp.ProfilePage(self.driver)
        self.course_page = cp.CoursesPage(self.driver)

    def tearDown(self):

        self.profile_page.unsubscribe_from_course_in_profile()
        self.driver.quit()

    def test_subscribe_on_course_as_user(self):

        """ Test for checking posibility to subscribe on course as user"""
        self.login_page.sign_in_as(**lp.VALID_DATA)
        self.course_page.subscribe_on_test_course()
        self.assertTrue(self.course_page.if_subscribe_course_present_in_profile(),
                        msg = 'subscribed course is not found')

    def test_subscribe_on_course_as_trainer(self):

        """ Test for checking posibility to subscribe on course as trainer"""
        self.login_page.sign_in_as(**lp.TRAINER_DATA)
        self.course_page.subscribe_on_test_course()
        self.assertTrue(self.course_page.if_subscribe_course_present_in_profile(),
                        msg='subscribed course is not found')

    def test_subscribe_on_course_as_moderator(self):

        """ Test for checking posibility to subscribe on course as moderator"""
        self.login_page.sign_in_as(**lp.MODERATOR_DATA)
        self.course_page.subscribe_on_test_course()
        self.assertTrue(self.course_page.if_subscribe_course_present_in_profile(),
                        msg='subscribed course is not found')


    def test_subscribe_on_course_as_admin(self):

        """ Test for checking posibility to subscribe on course as admin"""
        self.login_page.sign_in_as(**lp.ADMIN_DATA)
        self.course_page.subscribe_on_test_course()
        self.assertTrue(self.course_page.if_subscribe_course_present_in_profile(),
                        msg='subscribed course is not found')


if __name__ == "__main__":
    unittest.main(verbosity=2)
