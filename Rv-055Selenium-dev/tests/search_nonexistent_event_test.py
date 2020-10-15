"""test case to check that search returns no event and appropriate messages
appears when user searches pattern is not suitable to any event."""
import unittest
from selenium import webdriver
from pages import events_page as ep
import time


class search_nonexistent_event(unittest.TestCase):
    """check that search returns no event and appropriate messages
    appears when user searches pattern is not suitable to any event."""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.events_page = ep.EventsPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_search_nonexistent_event(self):
        self.events_page.go_to()
        self.events_page.search_event('Random')
        self.assertTrue(self.events_page.is_no_events_message_on_page())


if __name__ == "__main__":
    unittest.main(verbosity=2)
