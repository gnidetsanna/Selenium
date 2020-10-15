"""Test cases for Black Box testing of Possibility
for user to see the event details"""

import unittest
from selenium import webdriver
from pages import event_details_page as edp


class EventsDetails(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.event_details_page = edp.EventsDetailsPage(self.driver)

    def tearDown(self):
        self.driver.close()


    def test_event_details_text_about(self):
        self.event_details_page.go_to()
        self.event_details_page.click_on_event()
        self.assertTrue(self.event_details_page.is_text_about_presented())

    def test_event_details_person_title(self):
        self.event_details_page.go_to()
        self.event_details_page.click_on_event()
        self.assertTrue(self.event_details_page.is_person_title_presented())

    def test_event_details_location_title(self):
        self.event_details_page.go_to()
        self.event_details_page.click_on_event()
        self.assertTrue(self.event_details_page.is_location_title_presented())

    def test_event_details_date_title(self):
        self.event_details_page.go_to()
        self.event_details_page.click_on_event()
        self.assertTrue(self.event_details_page.is_date_title_presented())


if __name__ == "__main__":
    unittest.main(verbosity=2)