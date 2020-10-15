"""Class for the event edit page with methods which are used for testing"""
from pages import base_page
from pages.base_page import BasePage
from locators.event_edit_locators import EventEditLocators as locators
import os


class EventEditPage(BasePage):
    """Class for the event edit page with methods which are used for testing"""

    def assign_name(self, text):
        """metod to assign name"""
        self.fill_in_text_field_by_css(locators.EVENT_NAME_FIELD, text)

    def assign_category_other(self):
        """metod to assign category other"""
        self.click_on_element_by_css(locators.EVENT_CATEGORY)
        self.click_on_element_by_css(locators.EVENT_CATEGORY_OTHER)

    def assign_description(self, text):
        """metod to assign description"""
        self.fill_in_text_field_by_css(locators.EVENT_DESCRIPTION_FIELD, text)

    def assign_location(self, text):
        """metod to assign location"""
        self.fill_in_text_field_by_css(locators.LOCATION_FIELD, text)

    def add_image(self):
        """metod to add image"""
        self.find_element_by_css(locators.CHOOSE_FILE_BUTTON_CSS).send_keys(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"media","image_for_events.jpg"))
        self.click_on_element_by_css(locators.UPLOAD_IMAGE_CSS)

    def save_all(self):
        """metod to save all changes"""
        self.click_on_element_by_css(locators.SAVE_ALL_CSS)
