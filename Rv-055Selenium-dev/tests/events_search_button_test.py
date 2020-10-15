""" Test cases to verify Events search icon functionality """

import unittest
from selenium import webdriver
from pages import events_page as ep
from locators.events_locators import EventsPageLocators as epl


class EventsSearchButton(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.events_page = ep.EventsPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_events_search_button_tip(self):
        """Test to verify search button tip appears"""
        self.events_page.go_to()
        self.events_page.is_search_button_presented()
        self.events_page.click_on_search_button()
        self.events_page.clear_search_field()
        self.assertEqual(self.events_page.check_placeholder_text(), "What're you looking for?")

    def test_events_search_button(self):
        """Test to verify search button works and required item will be found"""
        self.events_page.go_to()
        self.events_page.is_search_button_presented()
        self.events_page.click_on_search_button()
        self.events_page.clear_search_field()
        self.events_page.fill_in_search_field_by_css()
        self.assertTrue(self.events_page.is_header_presented(epl.EVENT_HEADER))


if __name__ == "__main__":
    unittest.main(verbosity=2)
