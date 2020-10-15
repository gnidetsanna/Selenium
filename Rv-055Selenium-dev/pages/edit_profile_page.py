"""Class for the EditProfile page with methods which are used for testing"""
from selenium.common.exceptions import TimeoutException
import os
from pages import base_page
from pages.base_page import BasePage
from locators.edit_profile_locators import EditProfilePageLocators as ppl
import time

class EditProfilePage(BasePage):
    """docstring for ProfilePage."""

    def go_to(self):
        """method for redirecting to editprofile page"""
        self.driver.get(base_page.USER_SETTINGS_URL)
        time.sleep(1)

    def is_profile_avatar_present(self):
        """Method to check if profile info present"""
        try:
            self.click_on_element_by_css(ppl.EDIT_PROFILE_AVATAR_CSS)
            return True
        except TimeoutException:
            return False

    def click_on_change_icon_button(self):
        """Method used to click on 'change icon'
        button
        """
        self.click_on_element_by_css(ppl.EDIT_PROFILE_AVATAR_CSS)

    def click_on_choose_file_button(self):
        """Method used to click on 'change icon' button
        """

        self.find_element_by_css(ppl.CHOOSE_FILE_BUTTON_CSS).send_keys(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"media","testChangeIcon.png"))

    def upload_file_button(self):
        """Method used to click on 'Upload image' button
                """
        self.click_on_element_by_css(ppl.UPLOAD_IMAGE_CSS)

    def click_on_save_all_button(self):
        """Method used to click on 'Save all' button"""
        self.click_on_element_by_css(ppl.SAVE_ALL_CSS)

    def check_image(self):
        """Method used to return whether image has been changed or not"""
        element = self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div/div[1]/button/div/div/img")
        return "testChangeIcon" in element.get_attribute('src')

    def change_name(self, value):
        self.clear_text_field_by_css(ppl.NAME_FIELD)
        self.fill_in_text_field_by_css(ppl.NAME_FIELD, value)
        self.click_on_element_by_css(ppl.SAVE_ALL_BUTTON)

    def change_surname(self, value):
        self.clear_text_field_by_css(ppl.SURNAME_FIELD)
        self.fill_in_text_field_by_css(ppl.SURNAME_FIELD, value)
        self.click_on_element_by_css(ppl.SAVE_ALL_BUTTON)

    def change_login(self, value):
        self.clear_text_field_by_css(ppl.LOGIN_FIELD)
        self.fill_in_text_field_by_css(ppl.LOGIN_FIELD, value)
        self.click_on_element_by_css(ppl.SAVE_ALL_BUTTON)

    def change_location(self,value):
        self.find_element_by_css(ppl.LOCATION_FIELD_CSS)
        self.driver.execute_script("document.querySelector('input.location-search-input').value=''")
        self.fill_in_text_field_by_css(ppl.LOCATION_FIELD_CSS, value)
        #self.click_on_element_by_css(ppl.SAVE_ALL_CSS)

    def change_phone(self, value):
        self.clear_text_field_by_css(ppl.CONTACT_FIELD_CSS)
        self.fill_in_text_field_by_css(ppl.CONTACT_FIELD_CSS, value)
        #self.click_on_element_by_css(ppl.SAVE_ALL_CSS)

    def send_request_to_become_trainer(self):
        """Method used to send request to become a trainer"""
        self.click_on_element_by_css(ppl.WANT_TO_BECOME_TRAINER_BUTTON)

