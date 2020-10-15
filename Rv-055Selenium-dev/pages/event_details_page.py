"""Class for the event details page with methods which are used for testing"""
from selenium.common.exceptions import TimeoutException
from pages.events_page import EventsPage
from locators.events_locators import EventsPageLocators as epl
from pages import base_page


class EventsDetailsPage(EventsPage):
    """docstring for EventsPage."""

    def is_text_about_presented(self):
        """ Check 'About' text present """
        try:
            self.find_element_by_css(epl.EVENT_DETAILS_TEXT)
            return True
        except TimeoutException:
            return False

    def is_person_title_presented(self):
        """Check person title present"""
        try:
            self.find_element_by_css(epl.EVENT_DETAILS_PERSON)
            return True
        except TimeoutException:
            return False

    def is_location_title_presented(self):
        """Check location title present"""
        try:
            self.find_element_by_css(epl.EVENT_DETAILS_LOCATION)
            return True
        except TimeoutException:
            return False

    def is_date_title_presented(self):
        """Check date title present"""
        try:
            self.find_element_by_css(epl.EVENT_DETAILS_DATE)
            return True
        except TimeoutException:
            return False

    def join_to_event(self):
        if not self.is_user_join_to_this_event():
            self.click_on_element_by_css(epl.JOIN_TO_EVENT)
        else:
            return "User is already joined to this event"

    def is_user_join_to_this_event(self):
        try:
            base_page.WebDriverWait(self.driver, 3).until(
                base_page.EC.text_to_be_present_in_element(
                    epl.JOIN_TO_EVENT, "Leave the event"))
            return True
        except TimeoutException:
            return False

    def leave_event(self):
        if self.is_user_join_to_this_event():
            self.click_on_element_by_css(epl.JOIN_TO_EVENT)
        else:
            return "User no join to this event"

    def check_title(self):
        return self.find_element_by_css(epl.EVENT_DETAILS_TITLE).text
