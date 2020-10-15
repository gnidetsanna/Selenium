"""Class for the event create page with methods which are used for testing"""
from pages import base_page
from pages.base_page import BasePage
from locators.event_create_locators import EventCreateLocators as locators


class EventCreatePage(BasePage):
    """Class for the event create page with methods which are used for testing"""

    def create_event(self):
        """metod to go to creat new event"""
        self.click_on_element_by_css(locators.CREATE_VENT)

    def go_to(self):
        self.driver.get(base_page.EVENT_CREATE_PAGE_URL)
