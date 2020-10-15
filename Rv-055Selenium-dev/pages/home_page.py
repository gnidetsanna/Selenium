"""Class for the Home page with methods which are used for testing"""
from selenium.common.exceptions import TimeoutException
from pages import base_page
from pages.base_page import BasePage
from locators.homepage_locators import HomePageLocators as Locators


class HomePage(BasePage):
    """docstring for HomePage."""

    def click_on_nav_sign_in_button(self):
        """Method for clicking on the sign in button"""
        self.click_on_element_by_css(Locators.NAV_SIGN_IN)

    def click_on_body_sign_in_button(self):
        """Method for clicking on the body sign in button"""
        self.click_on_element_by_css(Locators.SIGN_IN_BODY)

    def click_on_body_sign_up_button(self):
        """Method for clicking on the body sign up button"""
        self.click_on_element_by_css(Locators.SIGN_UP_BODY)

    def click_on_left_slide_button(self):
        """Method for clicking on the left slide button"""
        self.click_on_element_by_css(Locators.LEFT_SLIDE_BUTTON)

    def click_on_right_slide_button(self):
        """Method for clicking on the right slide button"""
        self.click_on_element_by_css(Locators.RIGHT_SLIDE_BUTTON)

    def click_on_event_details_button(self):
        """Method for clicking on event details button"""
        self.click_on_element_by_css(Locators.EVENT_DETAILS_BUTTON)

    def click_on_more_events_button(self):
        """Method for clicking on the more events button """
        self.click_on_element_by_css(Locators.MORE_EVENTS_BUTTON)

    def click_on_trainer_one_button(self):
        """Method for clicking on the trainer one button"""
        self.click_on_element_by_css(Locators.TRAINER_ONE_BUTTON)

    def click_on_trainer_two_button(self):
        """Method for clicking on the trainer two button"""
        self.click_on_element_by_css(Locators.TRAINER_TWO_BUTTON)

    def click_on_trainer_three_button(self):
        """Method for clicking on the trainer three button"""
        self.click_on_element_by_css(Locators.TRAINER_THREE_BUTTON)

    def click_on_trainer_four_button(self):
        """Method for clicking on the trainer four button"""
        self.click_on_element_by_css(Locators.TRAINER_FOUR_BUTTON)

    def click_on_course_photo(self):
        """Method for clicking on the course photo"""
        self.click_on_element_by_css(Locators.COURSE_PHOTO)

    def click_on_course_title(self):
        """Method for clicking on the course title"""
        self.click_on_element_by_css(Locators.COURSE_TITLE)

    def click_on_course_rate(self):
        """Method for clicking on the course rate"""
        self.click_on_element_by_css(Locators.COURSE_RATE)

    def click_on_course_description(self):
        """Method for clicking on the course description"""
        self.click_on_element_by_css(Locators.COURSE_DESCRIPTION)

    def click_on_more_courses_button(self):
        """Method for clicking on the more courses button"""
        self.click_on_element_by_css(Locators.MORE_COURSES_BUTTON)

    def click_on_sign_up_body_second(self):
        """Method for clicking on the second body sign up button"""
        self.click_on_element_by_css(Locators.SIGN_UP_BODY_SECOND)

    def click_on_sign_in_body_second(self):
        """Methods for clicking on the second body sign in button"""
        self.click_on_element_by_css(Locators.SIGN_IN_BODY_SECOND)

    def nav_sign_in_button_presence(self):
        """Method for checking the presence of a navigation sign in button on the page"""
        try:
            self.find_element_by_css(Locators.NAV_SIGN_IN)
            return True
        except TimeoutException:
            return False

    def body_sign_in_button_presence(self):
        """Method for checking the presence of a body sign in button on the page"""
        try:
            self.find_element_by_css(Locators.SIGN_IN_BODY)
            return True
        except TimeoutException:
            return False

    def body_sign_up_button_presence(self):
        """Method for checking the presence of a body sign up button on the page"""
        try:
            self.find_element_by_css(Locators.SIGN_UP_BODY)
            return True
        except TimeoutException:
            return False

    def left_slide_button_presence(self):
        """Method for checking the presence of left slide button on the page"""
        try:
            self.find_element_by_css(Locators.LEFT_SLIDE_BUTTON)
            return True
        except TimeoutException:
            return False

    def right_slide_button_presence(self):
        """Method for checking the presence of the right slide button oh the page"""
        try:
            self.find_element_by_css(Locators.RIGHT_SLIDE_BUTTON)
            return True
        except TimeoutException:
            return False

    def event_details_button_presence(self):
        """Method for checking the presence of the event details button on the page"""
        try:
            self.find_element_by_css(Locators.EVENT_DETAILS_BUTTON)
            return True
        except TimeoutException:
            return False

    def more_events_button_presence(self):
        """Method for checking the presence of the more events button presence"""
        try:
            self.find_element_by_css(Locators.MORE_EVENTS_BUTTON)
            return True
        except TimeoutException:
            return False

    def trainer_one_button_presence(self):
        """Method for checking the presence of the trainer one button on the page"""
        try:
            self.find_element_by_css(Locators.TRAINER_ONE_BUTTON)
            return True
        except TimeoutException:
            return False

    def trainer_two_button_presence(self):
        """Method for checking the presence of the trainer two button on the page"""
        try:
            self.find_element_by_css(Locators.TRAINER_TWO_BUTTON)
            return True
        except TimeoutException:
            return False

    def trainer_three_button_presence(self):
        """Method for checking the presence of the trainer three button on the page"""
        try:
            self.find_element_by_css(Locators.TRAINER_THREE_BUTTON)
            return True
        except TimeoutException:
            return False

    def trainer_four_button_presence(self):
        """Method for checking the presence of the trainer four button on the page"""
        try:
            self.find_element_by_css(Locators.TRAINER_FOUR_BUTTON)
            return True
        except TimeoutException:
            return False

    def course_photo_presence(self):
        """Method for checking the presence of the course photo on the page"""
        try:
            self.find_element_by_css(Locators.COURSE_PHOTO)
            return True
        except TimeoutException:
            return False

    def course_title_presence(self):
        """Method for checking the presence of the course title on the page"""
        try:
            self.find_element_by_css(Locators.COURSE_TITLE)
            return True
        except TimeoutException:
            return False

    def course_rate_presence(self):
        """Method for checking the presence of the course rate on the page"""
        try:
            self.find_element_by_css(Locators.COURSE_RATE)
            return True
        except TimeoutException:
            return False

    def course_description_presence(self):
        """Method for checking the presence of the course details on the page"""
        try:
            self.find_element_by_css(Locators.COURSE_DESCRIPTION)
            return True
        except TimeoutException:
            return False

    def more_courses_button_presence(self):
        """Method for checking the presence of the more courses button on the page"""
        try:
            self.find_element_by_css(Locators.MORE_COURSES_BUTTON)
            return True
        except TimeoutException:
            return False

    def sign_up_body_second_button_presence(self):
        """Method for checking the presence of the second body sign up button on the page"""
        try:
            self.find_element_by_css(Locators.SIGN_UP_BODY_SECOND)
            return True
        except TimeoutException:
            return False

    def sign_in_body_second_presence(self):
        """Method for checking the presence of the second body sign in button on th page"""
        try:
            self.find_element_by_css(Locators.SIGN_IN_BODY_SECOND)
            return True
        except TimeoutException:
            return False

    def go_to_home_page(self):
        """Method for redirecting to home page"""
        self.driver.get(base_page.BASE_URL)
