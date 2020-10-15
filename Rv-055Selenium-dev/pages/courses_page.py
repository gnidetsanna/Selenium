"""Class for Courses page with methods which are used for testing."""
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import WebDriverException
from pages import base_page
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.courses_locators import CoursesPageLocators as Locators
from locators.course_details_locators import CourseDetailsLocators as Locators
from locators import course_filter_locators as cpl
from selenium.webdriver.support import expected_conditions as EC
from pages.profile_page import ProfilePage
from locators.profile_locators import ProfilePageLocators as ppl

class CoursesPage(BasePage):

    def click_on_search_icon(self):
        """Method for clicking on search icon."""
        self.click_on_element_by_css(Locators.SEARCH_ICON)

    def go_to(self):
        """Method for redirecting to courses page."""
        self.driver.get(base_page.COURSES_PAGE_URL)

    def is_page_loaded(self, address):
        """Method to check if courses page is loaded."""
        try:
            self.wait.until(base_page.EC.url_to_be(address))
            return True
        except TimeoutException:
            return False

    def find_search_icon_by_css(self, by_css):
        """Method for finding search icon on the page"""
        self.find_element_by_css(Locators.SEARCH_ICON)

    def fill_in_text_field_by_css(self, by_css, text):
        """Method for filling in the text field with text"""
        self.wait.until(EC.visibility_of_element_located(by_css)
                        ).send_keys(text)

    def is_valid_text_on_page(self):
        """Method for finding specific text on the page"""
        try:
            self.find_element_by_css(Locators.COURSE_DESCRIPTION_CARD)
            return True
        except TimeoutException:
            return False

    def click_on_course_header(self):
        """Method for clicking on course header on the course page."""
        self.click_on_element_by_css(Locators.COURSE_HEADER)

    def find_course_header(self):
        """Method for finding course header."""
        self.find_element_by_css(Locators.COURSE_HEADER)

    def second_click_on_search_icon(self):
        """Method for second clicking on search icon"""
        self.click_on_element_by_css(Locators.SMALL_SEARCH_ICON)

    def is_search_fild_active(self):
        """Method for check is search field active"""
        try:
            self.click_on_element_by_css(Locators.SMALL_SEARCH_ICON)
            return True
        except WebDriverException:
            return False

    def is_courses_on_page(self):
        """Method for check is at least 1 course on page"""
        try:
            self.find_element_by_css(Locators.COURSE_DESCRIPTION_CARD)
            return True
        except TimeoutException:
            return False

    def go_to_CourseSearchPage(self):

        """Method for redirecting on the course search page"""
        self.driver.get(base_page.COURSES_PAGE_URL)

    def click_on_filter_course_button(self):

        """Method for clicking on the filter course button"""
        self.click_on_element_by_css(cpl.COURSE_FILTER_BUTTON)

    def click_on_filter_music_checkbox(self):

        """Method for choosing music filter category"""
        self.click_on_element_by_css(cpl.FILTER_BY_MUSIC_CHECKBOX)

    def click_on_filter_sport_checkbox(self):

        """Method for choosing sport filter category"""
        self.click_on_element_by_css(cpl.FILTER_BY_SPORT_CHECKBOX)

    def click_on_filter_software_checkbox(self):

        """Method for choosing software filter category"""
        self.click_on_element_by_css(cpl.FILTER_BY_SOFTWARE_CHECKBOX)

    def click_on_filter_status_open(self):

        """Method for choosing opened courses"""
        self.click_on_element_by_css(cpl.FILTER_BY_STATUS_OPEN)

    def click_on_filter_status_closed(self):

        """Method for choosing closed courses"""
        self.click_on_element_by_css(cpl.FILTER_BY_STATUS_CLOSED)

    def click_on_filter_cost_free(self):

        """Method for choosing free courses"""
        self.click_on_element_by_css(cpl.FREE_COST_FILTER)

    def click_on_filter_cost_paid(self):

        """Method for choosing paid courses"""
        self.click_on_element_by_css(cpl.PAID_COST_FILTER)

    def close_filter_window(self):

        """Method closing filter window"""
        self.click_on_element_by_css(cpl.CLOSE_FILTER_WINDOW)

    def click_on_first_course_on_page(self):

        """Method for choosing first course on page"""
        self.click_on_element_by_css(cpl.FIRST_COURSE_ON_PAGE)

    def is_first_course_on_page_of_music_category(self):

        """Method for checking first course on page of music category"""
        try:
            self.find_element_by_xpath(cpl.MUSIC_COURSE_CATEGORY)
            return True
        except TimeoutException:
            return False

    def is_first_course_on_page_of_sport_category(self):

        """Method for checking first course on page of sport category"""
        try:
            self.find_element_by_xpath(cpl.SPORT_COURSE_CATEGORY)
            return True
        except TimeoutException:
            return False

    def is_first_course_on_page_of_software_category(self):

        """Method for checking first course on page of software category"""
        try:
            self.find_element_by_xpath(cpl.SOFTWARE_COURSE_CATEGORY)
            return True
        except TimeoutException:
            return False

    def is_subscribe_button_present_in_course_page(self):

        """Method for checking presents of the subscribe button """
        try:
            self.find_element_by_css(cpl.SUBSCRIBE_BUTTON)
            return True
        except TimeoutException:
            return False

    def is_open_icon_present_in_course_page(self):

        """Method for checking presents of the open course icon """
        try:
            self.find_element_by_xpath(cpl.OPEN_COURSE_ICON)
            return True
        except TimeoutException:
            return False

    def is_closed_icon_present_in_course_page(self):

        """Method for checking presents of the closed course icon """
        try:
            self.find_element_by_xpath(cpl.CLOSED_COURSE_ICON)
            return True
        except TimeoutException:
            return False

    def is_the_course_free(self):

        """Method for checking if the course is costless """
        try:
            self.find_element_by_xpath(cpl.COURSE_COSTS_ZERO)
            return True
        except TimeoutException:
            return False

    def is_course_on_page_of_music_category(self):

        """Method for checking if the music course is present on page """
        try:
            self.find_element_by_xpath(cpl.MUSIC_COURSE_ON_PAGE)
            return True
        except TimeoutException:
            return False

    def is_course_on_page_of_sport_category(self):

        """Method for checking if the sport course is present on page """
        try:
            self.find_element_by_xpath(cpl.SPORT_COURSE_ON_PAGE)
            return True
        except TimeoutException:
            return False

    def is_course_on_page_of_software_category(self):

        """Method for checking if the software course is present on page """
        try:
            self.find_element_by_xpath(cpl.SOFTWARE_COURSE_ON_PAGE)
            return True
        except TimeoutException:
            return False

    def is_course_on_page_of_other_category(self):

        """Method for checking if the other course is present on page """
        try:
            self.find_element_by_xpath(cpl.OTHER_COURSE_ON_PAGE)
            return True
        except TimeoutException:
            return False

    def if_subscribe_course_present_in_profile(self):

        """Method for checking presents follow course in profile page"""
        self.profile_page = ProfilePage(self.driver)
        self.profile_page.go_to()
        self.profile_page.click_on_following_courses()
        try:
            self.find_element_by_xpath(cpl.TEST_COURSE)
        except NoSuchElementException:
            return False
        return True

    def click_on_subscribe_course_button(self):

        """Method for clicking on subscribe course button """
        self.click_on_element_by_css(cpl.SUBSCRIBE_BUTTON)

    def click_on_first_opened_course(self):

        """Method for clicking on first open course on page """
        self.go_to_CourseSearchPage()
        self.click_on_filter_course_button()
        self.click_on_filter_status_open()
        self.close_filter_window()
        self.click_on_first_course_on_page()

    def subscribe_on_test_course(self):

        """Method for subscribing on the test course """
        self.go_to_CourseSearchPage()
        self.click_on_filter_course_button()
        self.click_on_filter_sport_checkbox()
        self.click_on_filter_status_open()
        self.close_filter_window()
        self.click_on_element_by_link_text("Test_subscribe_course")
        self.click_on_subscribe_course_button()
