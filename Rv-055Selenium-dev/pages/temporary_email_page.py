from locators.temporary_email_locators import TemporaryEmailPageLocators as tep
from pages.base_page import BasePage

TEMPORARY_EMAIL_CLIENT = 'https://temp-mail.org/'


class TemporaryEmailPage(BasePage):
    """docstring for TemporaryEmailPage"""

    def get_temporary_email(self):
        """Method for getting temporary email account"""
        self.click_on_element_by_css(tep.COPY_EMAIL_ADDRESS_BUTTON)

    def open_email(self):
        """Method for opening email"""
        self.driver.execute_script("window.scrollTo(0, 700)")
        self.click_on_element_by_css(tep.OPEN_EMAIL_BUTTON)

    def activate_account(self):
        """Method for activating user account"""
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.click_on_element_by_css(tep.ACTIVATION_LINK)
        self.click_on_element_by_css(tep.ACTIVATION_BUTTON)
