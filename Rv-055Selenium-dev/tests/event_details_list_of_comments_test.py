"""Test cases for Black Box testing of Possibility
for user to see the list of comments in event details"""

import unittest
from selenium import webdriver
from pages import event_details_page as edp
from pages import events_page as ep
from pages import base_page as bp
from pages import login_page as lp
from locators.events_locators import EventsPageLocators as epl


class EventsDetailsComments(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.event_details_page = edp.EventsDetailsPage(self.driver)
        self.events_page = ep.EventsPage(self.driver)
        self.login_page = lp.LoginPage(self.driver)
        self.base_page = bp.BasePage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_event_details_comments_list(self):
        """Test to verify the list of comments appear"""
        self.event_details_page.go_to()
        self.event_details_page.click_on_event()
        self.assertTrue(self.events_page.is_details_comment_list_present())

    def test_event_all_comments_appear(self):
        """Test to verify use can see the list of all comments"""
        self.event_details_page.go_to()
        self.event_details_page.click_on_event()
        self.assertTrue(self.base_page.presence_of_all_elements_by_css(epl.ALL_COMMENTS_SELECTOR))


if __name__ == "__main__":
    unittest.main()
