"""Test cases for Black Box testing of Possibility
for user to manage own profile"""
import unittest
from selenium import webdriver
from pages import login_page as lp
from pages import profile_page as pp
from pages import base_page
from helpers import login_helpers
from helpers import read_mail
import helpers.settings as settings
from locators.login_locators import LoginPageLocators as lpl


class UserManageProfile(unittest.TestCase):
    """Docstring for UserManageProfile."""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.login_page = lp.LoginPage(self.driver)
        self.profile_page = pp.ProfilePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_profile_info(self):
        """test possibility to view profile page as authorized user #316 #317"""
        self.login_page.sign_in_as(**lp.VALID_DATA)
        self.assertTrue(self.profile_page.is_profile_info_present(),
                        msg='profile info not found')

    def test_password_change(self):
        """test possibility to change password #310"""
        def start_test(new_pass, base_case=None):
            if base_case:
                credensials = lp.TRAINER_DATA.copy()
                credensials.update(password=new_pass)
                new_pass = lp.TRAINER_DATA['password']
            else:
                credensials = lp.TRAINER_DATA.copy()
            self.login_page.sign_in_as(**credensials)
            self.assertTrue(
                self.login_page.is_page_loaded(base_page.PROFILE_PAGE_URL),
                msg="password change failed, can't load profile page")
            self.driver.execute_script(
                'document.querySelector("div .edit-tool").click()')
            self.profile_page.fill_in_new_password(new_pass)
            self.profile_page.click_change_password()
            self.login_page.sign_out()
            self.login_page.is_sign_up_button_present()
            if base_case:
                return
            start_test(new_pass, True)

        new_pass = login_helpers.get_random_pass()
        start_test(new_pass)

    def test_password_reset(self):
        """test possibility to reset password #222"""
        self.login_page.go_to()
        self.login_page.click_on_sign_in_button()
        self.login_page.click_on_forgot_password()
        self.login_page.fill_in_text_field_by_css(lpl.RESET_PASS_FORM_CSS,
                                                  settings.EMAIL_HOST_USER)
        self.login_page.click_on_resset_button()
        _, link = read_mail.read_mail()
        self.driver.get(link)
        self.login_page.fill_in_new_password(lp.NEW_TRAINER['password'])
        self.login_page.click_on_resset_button()
        self.login_page.sign_in_as(**lp.NEW_TRAINER)
        self.assertTrue(
            self.login_page.is_page_loaded(base_page.PROFILE_PAGE_URL),
            msg="profile page failed to load")

    def test_have_courses(self):
        """As the authorized trainer of the system,
        I want to have a list of my own courses #232
        """
        self.login_page.sign_in_as(**lp.TRAINER_DATA)
        self.profile_page.click_on_own_courses()
        self.assertTrue(
            self.profile_page.is_courses_present(),
            msg="courses not found")


if __name__ == "__main__":
    unittest.main()
