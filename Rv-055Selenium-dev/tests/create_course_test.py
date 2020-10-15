"""Test cases for testing of Possibility
for trainer to create courses"""
import unittest
from selenium import webdriver
from pages import login_page as lp
from pages import base_page as bp
from pages import courses_page as cp
from pages import profile_page as pp
from pages import create_course_page as cc
from locators.courses_locators import CoursesPageLocators as cpl


class CreateCourseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = lp.LoginPage(self.driver)
        self.profile_page = pp.ProfilePage(self.driver)
        self.course_page = cc.NewCoursePage(self.driver)
        self.base_page = bp.BasePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_trainer_create_course(self):
        Course_info = {"Name": "Cycling",
                       "About": "This is a cycling training",
                       "Limit": 9,
                       "Duration": 1,
                       "Start_day": "12072020",
                       "Start_time": "1230PM",
                       "Price": 35,
                       "Location": "Rivne",
                       "Trainer": "Sonya Alcock"}
        """As the authorized trainer of the system,
            I want to have a possibility to create a course"""
        self.login_page.sign_in_as(**lp.TRAINER_DATA)
        self.course_page.create_new_course()
        self.course_page.fill_course_name(Course_info['Name'])
        self.course_page.choose_icon()
        self.course_page.fill_about_course_field(Course_info['About'])
        self.course_page.fill_limit_members_of_course(Course_info['Limit'])
        self.course_page.fill_course_duration(Course_info['Duration'])
        self.course_page.fill_course_start_day(Course_info['Start_day'])
        self.course_page.fill_course_start_time(Course_info['Start_time'])
        self.course_page.fill_course_price(Course_info['Price'])
        self.course_page.fill_course_location(Course_info['Location'])
        self.course_page.click_on_course_category()
        self.course_page.click_on_course_status()
        self.course_page.click_create_course()
        self.driver.execute_script("window.scrollTo( document.body.scrollHeight, 0);")
        self.course_page.click_on_search_icon()
        self.base_page.fill_in_text_field_by_css(cpl.SEARCH_ICON, Course_info['Name'])
        self.course_page.second_click_on_search_icon()
        self.course_page.find_new_course()
        self.assertTrue(Course_info['Trainer'] in self.course_page.is_valid_trainer_of_course())


if __name__ == "__main__":
    unittest.main(verbosity=2)
