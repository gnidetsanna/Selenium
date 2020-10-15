"""Class for Courses page with methods which are used for testing."""

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.homepage_locators import HomePageLocators as hpl
from locators.course_create_locators import NewCourseLocators as ncl
from locators.courses_locators import CoursesPageLocators as cp
import os

class NewCoursePage(BasePage):
    """Class with methods used to test Create course page"""


    def create_new_course(self):
        """Method for creating new course"""
        self.click_on_element_by_css(hpl.USER_MENU_BUTTON)
        self.click_on_element_by_css(hpl.CREATE_COURSE_BUTTON)

    def fill_course_name(self, value):
        """Method for filling new course"""
        self.fill_in_text_field_by_css(ncl.COURSE_NAME_BUTTON, value)

    def choose_icon(self):
        """Method for choosing icon for anew course"""
        input_field = self.driver.find_element_by_css_selector("form input[type='file']")
        file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"media","testChangeIcon.png")
        input_field.send_keys(file_path)

    def fill_about_course_field(self, value):
        """Method for filling "About" of new course"""
        self.fill_in_text_field_by_css(ncl.ABOUT_BUTTON, value)

    def fill_limit_members_of_course(self, value):
        """Method for filling "Limit of members" of new course"""
        self.fill_in_text_field_by_css(ncl.MEMBERS_BUTTON, value)

    def fill_course_duration(self, value):
        """Method for filling "Duration" of new course"""
        self.fill_in_text_field_by_css(ncl.DURATION_BUTTON,value)

    def fill_course_start_day(self, value):
        """Method for filling "Start day" of new course"""
        self.fill_in_text_field_by_css(ncl.START_DAY_BUTTON, value)

    def fill_course_start_time(self, value):
        """Method for filling "Start time" of new course"""
        self.fill_in_text_field_by_css(ncl.START_TIME_BUTTON, value)

    def fill_course_price(self, value):
        """Method for filling "Price" of new course"""
        self.fill_in_text_field_by_css(ncl.PRICE_BUTTON, value)

    def fill_course_location(self, value):
        """Method for filling "Location" of new course"""
        self.fill_in_text_field_by_css(ncl.LOCATION_BUTTON, value)

    def click_on_course_category(self):
        """Method for filling "Category" of new course"""
        self.find_element_by_xpath("//select[@name='category']/option[text()='Sport']").click()

    def click_on_course_status(self):
        """Method for filling "Course status" of new course"""
        self.find_element_by_xpath("//select[@name='category']/option[text()='In Progress']").click()
        self.find_element_by_xpath("//*[@id='root']/div/main/form/div/div[3]/div/div[1]/select[2]").click()

    def click_create_course(self):
        """Method for clicking 'Create course' button"""
        self.wait.until(EC.element_to_be_clickable(ncl.CREATE_COURSE_BUTTON)).click()


    def click_on_search_icon(self):
        """Method for clicking on search icon."""
        self.wait.until(EC.element_to_be_clickable(cp.SEARCH_ICON)).click()

    def second_click_on_search_icon(self):
        """Method for clicking on search icon second time."""
        self.wait.until(EC.element_to_be_clickable(cp.SMALL_SEARCH_ICON)).click()

    def find_new_course(self):
        """Method for finding description card of new course"""
        self.find_any_element_by_css(cp.COURSE_DESCRIPTION_CARD)

    def is_valid_trainer_of_course(self):
        """Method for extracting trainer`s name from course description"""
        return self.find_element_by_xpath("//*[@id='page-wrap']/div/div[4]/div[2]/div/div/a/"
                                          "div/div[2]/p/p[3]").text



