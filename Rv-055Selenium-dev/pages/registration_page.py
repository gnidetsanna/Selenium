from pages import base_page
from locators.homepage_locators import HomePageLocators as hpl
from locators.registration_locators import RegistrationPageLocators as rpl
import random
from selenium.webdriver.common.keys import Keys

CHARS_FOR_PASS = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
PASS_LENGTH = 8


def strong_password_generator():
    """function for generation strong password for sign-up"""
    password = ''
    for i in range(PASS_LENGTH):
        password += random.choice(CHARS_FOR_PASS)
    return password


class RegistationPage(base_page.BasePage):
    """docstring for RegistationPage"""

    def open_sign_up_window(self):
        """Method for opening sign-up window"""
        self.click_on_element_by_css(hpl.SIGN_UP_BODY)

    def mark_as_teacher(self):
        """Method for marking account like teacher"""
        self.click_on_element_by_css(rpl.TEACHER_MARK)

    def fill_in_email_field(self):
        """Method for filling in email text field"""
        self.email_field = self.find_element_by_css(rpl.INPUT_FIELD_EMAIL_REG)
        self.clear_text_field_by_css(rpl.INPUT_FIELD_EMAIL_REG)
        self.email_field.send_keys(Keys.CONTROL, 'v')
        self.email_address = self.find_element_by_css(rpl.INPUT_FIELD_EMAIL_REG).get_attribute("value")

    def fill_in_password_fields(self):
        """Method for filling in password text fields"""
        self.strong_password = strong_password_generator()
        self.clear_text_field_by_css(rpl.INPUT_FIELD_PASS_REG)
        self.fill_in_text_field_by_css(rpl.INPUT_FIELD_PASS_REG, self.strong_password)
        self.clear_text_field_by_css(rpl.INPUT_FIELD_CONFIRM_PASS_REG)
        self.fill_in_text_field_by_css(rpl.INPUT_FIELD_CONFIRM_PASS_REG, self.strong_password)

    def confirm_sign_up(self):
        """Method for clicking on sign-up button, confirming registration process"""
        self.click_on_element_by_css(rpl.CONFIRM_SIGN_UP_BUTTON)

    def create_dictionary_for_login(self):
        """Method for creating dictionary for testing and working with sing-in method"""
        self.data_for_sing_in = {"mail": self.email_address, "password": self.strong_password}
        return self.data_for_sing_in

    def is_teacher_functions_have_applied(self):
        """Method for checking if own courses menu applied to the teacher account"""
        return self.find_element_by_css(rpl.TEACHER_OWN_COURSES)
