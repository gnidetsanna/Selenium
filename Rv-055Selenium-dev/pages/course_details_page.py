"""Class for the course details page methods which ar used for the testing."""

from selenium.common.exceptions import TimeoutException
from locators.course_details_locators import CourseDetailsLocators as cdl
from pages.base_page import BasePage
from pages import base_page
from locators.courses_locators import CoursesPageLocators as cpl


class CourseDetailsPage(BasePage):

    def is_course_header_present(self):
        """Method for checking presence of course header with its title and status."""
        try:
            self.find_element_by_css(cdl.COURSE_DETAILS_HEADER)
            return True
        except TimeoutException:
            return False

    def is_short_course_info_present(self):
        """Method for checking the presence of the short course info on course details page."""
        try:
            self.find_element_by_css(cdl.SHORT_COURSE_INFO)
            return True
        except TimeoutException:
            return False

    def is_about_course_present(self):
        """Method for checking presence of 'about' column on course details page."""
        try:
            self.find_element_by_css(cdl.ABOUT_COURSE)
            return True
        except TimeoutException:
            return False

    def is_calendar_present(self):
        """Method for checking presence of calendar on course details page."""
        try:
            self.find_element_by_css(cdl.CALENDAR)
            return True
        except TimeoutException:
            return False

    def is_comment_section_present(self):
        """Method for checking presence of comment section ob course details page."""
        try:
            self.find_element_by_css(cdl.COMMENT_SECTION)
            return True
        except TimeoutException:
            return False

    def is_subscribe_button_present(self):
        """Method for checking presence of subscribe button on course details page."""
        try:
            self.find_element_by_css(cdl.SUBSCRIBE_BUTTON)
            return True
        except TimeoutException:
            return False

    def is_back_button_present(self):
        """Method checking presence of back button on course details page."""
        try:
            self.find_element_by_css(cdl.BACK_BUTTON)
            return True
        except TimeoutException:
            return False

    def go_to(self):
        """Method for redirecting to course details page."""
        self.driver.get(base_page.COURSE_DETAILS_PAGE_URL)

    def click_on_course(self):
        """Method for clicking on course header on the course page."""
        self.click_on_element_by_css(cpl.COURSE_HEADER)

    def find_course(self):
        """Method for finding course header."""
        self.find_element_by_css(cpl.COURSE_HEADER)

    def click_on_subscribe_button(self):
        """Method for clicking on subscribe button."""
        self.click_on_element_by_css(cdl.SUBSCRIBE_BUTTON)

    def message_unsubscribe_course(self):
        """Method for checking the appearing of
        confirmation message after unsubscription.
        """
        try:
            self.find_element_by_css(cdl.UNSUBSCRIBE_MESSAGE)
            return True
        except TimeoutException:
            return False

    def is_all_attributes_of_course_present(self):
        try:
            self.is_back_button_present()
            self.is_calendar_present()
            self.is_comment_section_present()
            self.is_course_header_present()
            self.is_short_course_info_present()
            self.is_about_course_present()
            self.is_subscribe_button_present()
            self.is_back_button_present()
            return True
        except TimeoutException:
            return False

    def is_user_subscribed_on_course(self):
        """Method for checking if user is subscribed on course."""
        try:
            base_page.WebDriverWait(self.driver, 3).until(
                base_page.EC.text_to_be_present_in_element(
                    cdl.SUBSCRIBE_BUTTON, "Unsubscribe"))
            return True
        except TimeoutException:
            return False

    def unsubscribe_from_course(self):
        """Method for unsubscribing from course."""
        if self.is_user_subscribed_on_course():
            self.click_on_subscribe_button()
        else:
            return "User in not subscribed on this course."

    def click_on_comment_button(self):
        self.click_on_element_by_css(cdl.COMMENT_BUTTON)

    def write_a_comment(self):
        """Method for writing a comment to course."""
        comment = "abracadabra"
        self.fill_in_text_field_by_css(cdl.COMMENT_SECTION, comment)
        return comment

    def find_comment(self):
        """Method for finding comment in comment section."""
        try:
            self.find_element_by_css(cdl.FIRST_COMMENT)
            return True
        except TimeoutException:
            return False
