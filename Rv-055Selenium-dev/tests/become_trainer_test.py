"""Test cases for Black Box testing of Possibility
for user to become a trainer"""

import unittest
from selenium import webdriver
from pages import login_page as lp
from pages import profile_page as pp
from pages import edit_profile_page as epp
from pages import base_page as bp
from locators.edit_profile_locators import EditProfilePageLocators as epl
from locators.moderator_dashboard_locators import ModeratorDashboardLocators as mdl
from locators.homepage_locators import HomePageLocators as hpl

class BecomeTrainer(unittest.TestCase):
    """Verify possibility for user to become trainer"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = lp.LoginPage(self.driver)
        self.profile_page = pp.ProfilePage(self.driver)
        self.edit_profile_page = epp.EditProfilePage(self.driver)
        self.base_page = bp.BasePage(self.driver)



    def tearDown(self):
        self.driver.close()


    def test_moderator_approve_user_request_to_be_trainer(self):
        """Method to approve request from user"""
        self.login_page.sign_in_as(**lp.VALID_DATA)
        self.login_page.is_page_loaded(bp.PROFILE_PAGE_URL)
        self.login_page.click_on_user_menu_button()
        self.edit_profile_page.go_to()
        self.base_page.click_on_element_by_css(epl.BECOME_TRAINER_BUTTON)
        self.login_page.sign_out()
        self.login_page.sign_in_as(**lp.MODERATOR_DATA)
        self.login_page.is_page_loaded(bp.PROFILE_PAGE_URL)
        self.login_page.click_on_user_menu_button()
        self.base_page.click_on_element_by_css(mdl.MODERATOR_DASHBOARD)
        self.base_page.click_on_element_by_css(mdl.ROLE_REQUESTS)
        self.base_page.click_on_element_by_css(mdl.CHECK_BOX)
        self.base_page.click_on_element_by_css(mdl.APPROVE_BUTTON)
        self.login_page.sign_out()
        self.login_page.sign_in_as(**lp.VALID_DATA)
        self.login_page.is_page_loaded(bp.PROFILE_PAGE_URL)
        self.login_page.click_on_user_menu_button()
        self.assertTrue(self.base_page.find_element_by_css(hpl.CREATE_COURSE_BUTTON))






if __name__ == "__main__":
    unittest.main(verbosity=2)