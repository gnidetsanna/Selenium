"""Class for the login form with methods which are used for testing"""
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from pages import base_page
from locators.login_locators import LoginPageLocators as lpl
from locators.homepage_locators import HomePageLocators as hpl

# user data for validation tests
VALID_DATA = {"mail": "test1@test.com", "password": "123456"}
ADMIN_DATA = {"mail":"youyoda.academy@gmail.com", "password":"123456"}
MODERATOR_DATA = {"mail":"test@test.com", "password":"123456"}
TRAINER_DATA = {"mail":"trainer1@test.com", "password":"123456"}
NEW_TRAINER = {"mail":"testforss27@gmail.com", "password":"123456"}


class LoginPage(BasePage):
    """Class with methods used to test Home page"""

    def is_login_form_is_present(self):
        """Method for assertion that 'login menu' is present"""
        try:
            self.find_element_by_css(lpl.LOGIN_FORM)
            return True
        except TimeoutException:
            return False

    def is_sign_up_button_present(self):
        """Method for assertion that 'Sign in' navbar button is present"""
        try:
            self.find_element_by_css(hpl.NAV_SIGN_IN)
            return True
        except TimeoutException:
            return False

    def is_profile_icon_present(self):
        """Method for assertion that 'profile_icon' is present"""
        try:
            self.find_element_by_css(hpl.PROFILE_ICON)
            return True
        except TimeoutException:
            return False

    def click_on_sign_in_button_confirm(self):
        """Method used to CONFIRM login operation
        after u typed email and password
        """
        self.click_on_element_by_css(lpl.CONFIRM_SIGN_IN_BUTTON_CSS)

    def click_on_forgot_password(self):
        """Method for clicking on forgot password href"""
        self.click_on_href_by_css(lpl.FORGOT_PASSWORD_CSS[1])

    def click_on_sign_in_button(self):
        """Method for clicking on login-nav-icon"""
        self.click_on_element_by_css(hpl.NAV_SIGN_IN)

    def click_on_user_menu_button(self):
        """Method for activating user menu"""
        self.click_on_element_by_css(hpl.USER_MENU_BUTTON)

    def clear_email_and_password_fields(self):
        """Method for clearing mail and password text fields"""
        self.clear_text_field_by_css(lpl.INPUT_FIELD_MAIL_CSS)
        self.clear_text_field_by_css(lpl.INPUT_FIELD_PASS_CSS)

    def fill_in_email_and_password_fields(self, **kwargs):
        """Method for filling in text fields with own data as dict"""
        self.fill_in_text_field_by_css(lpl.INPUT_FIELD_MAIL_CSS,
                                       kwargs.get("mail"))
        self.fill_in_text_field_by_css(lpl.INPUT_FIELD_PASS_CSS,
                                       kwargs.get("password"))

    def go_to(self):
        """Method for redirecting to home page"""
        self.driver.get(base_page.BASE_URL)

    def sign_out(self):
        """Signout method"""
        if self.is_profile_icon_present():
            self.click_on_user_menu_button()
            self.click_on_element_by_css(hpl.LOGOUT_BUTTON)
            self.is_sign_up_button_present()

    def sign_in_as(self, **kwargs):
        """Method for signing in with specified credentials"""
        self.go_to()
        self.click_on_sign_in_button()
        self.clear_email_and_password_fields()
        self.fill_in_email_and_password_fields(**kwargs)
        self.click_on_sign_in_button_confirm()
        self.is_page_loaded(base_page.PROFILE_PAGE_URL)

    def is_page_loaded(self, address):
        """Method to check does page loaded"""
        try:
            self.wait.until(base_page.EC.url_to_be(address))
            return True
        except TimeoutException:
            return False

    def fill_in_new_password(self, password):
        """Method to fill in new password during reset"""
        self.fill_in_text_field_by_css(lpl.INPUT_NEW_PASSWORD_CSS, password)
        self.fill_in_text_field_by_css(lpl.INPUT_RE_NEW_PASSWORD_CSS, password)

    def click_on_resset_button(self):
        """Method to click on submit button in reset password form"""
        self.click_on_element_by_css(lpl.BUTTON_RESET_PASS_CSS)
