"""test case to check the possibility to create event"""
import unittest
from selenium import webdriver
from pages import login_page as lp
from pages import profile_page as pp
from pages import event_create_page as ecp
from pages import event_edit_page as eep
from pages import events_page as ep
from pages import event_details_page as edp


class CreateEvent(unittest.TestCase):
    """create event"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = lp.LoginPage(self.driver)
        self.profile_page = pp.ProfilePage(self.driver)
        self.event_create_page = ecp.EventCreatePage(self.driver)
        self.event_edit_page = eep.EventEditPage(self.driver)
        self.events_page = ep.EventsPage(self.driver)
        self.event_details_page = edp.EventsDetailsPage(self.driver)
        self.login_page.sign_in_as(**lp.VALID_DATA)

    def tearDown(self):
        self.driver.close()

    def test_create_event(self):
        self.event_create_page.go_to()
        self.event_create_page.create_event()
        self.event_edit_page.assign_name("Test")
        self.event_edit_page.assign_category_other()
        self.event_edit_page.assign_description("Test event")
        self.event_edit_page.assign_location("Rivne")
        self.event_edit_page.add_image()
        self.event_edit_page.save_all()
        self.events_page.go_to()
        self.events_page.search_event("Test")
        self.events_page.go_to_first_event()
        self.assertEqual(self.event_details_page.check_title(), "Test")


if __name__ == "__main__":
    unittest.main(verbosity=2)
