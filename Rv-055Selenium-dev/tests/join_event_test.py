"""Test case to check the possibility to join the event"""
import unittest
from selenium import webdriver
from pages import login_page as lp
from pages import events_page as ep
from pages import profile_page as pp
from pages import event_details_page as edp


class JoinEvent(unittest.TestCase):
    """Join the event"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = lp.LoginPage(self.driver)
        self.profile_page = pp.ProfilePage(self.driver)
        self.events_page = ep.EventsPage(self.driver)
        self.event_details_page = edp.EventsDetailsPage(self.driver)

    def tearDown(self):
        self.event_details_page.leave_event()
        self.driver.close()

    def test_join_as_user(self):
        """Test to check the possibility to join the event as user"""
        self.login_page.sign_in_as(**lp.VALID_DATA)
        self.profile_page.is_profile_info_present()
        self.events_page.go_to()
        self.events_page.go_to_who_play_with_me()
        self.event_details_page.join_to_event()
        self.assertTrue(self.event_details_page.is_user_join_to_this_event())

    def test_join_as_moderator(self):
        """Test to check the possibility to join the event as moderator"""
        self.login_page.sign_in_as(**lp.MODERATOR_DATA)
        self.profile_page.is_profile_info_present()
        self.events_page.go_to()
        self.events_page.go_to_who_play_with_me()
        self.event_details_page.join_to_event()
        self.assertTrue(self.event_details_page.is_user_join_to_this_event())

    def test_join_as_admin(self):
        """Test to check the possibility to join the event as admin"""
        self.login_page.sign_in_as(**lp.ADMIN_DATA)
        self.profile_page.is_profile_info_present()
        self.events_page.go_to()
        self.events_page.go_to_who_play_with_me()
        self.event_details_page.join_to_event()
        self.assertTrue(self.event_details_page.is_user_join_to_this_event())

    def test_join_as_trainer(self):
        """Test to check the possibility to join the event as trainer"""
        self.login_page.sign_in_as(**lp.TRAINER_DATA)
        self.profile_page.is_profile_info_present()
        self.events_page.go_to()
        self.events_page.go_to_who_play_with_me()
        self.event_details_page.join_to_event()
        self.assertTrue(self.event_details_page.is_user_join_to_this_event())

    def test_join_as_unauthorized_user(self):
        """Test to check the possibility to join the event as unautorized user"""
        self.events_page.go_to()
        self.events_page.go_to_who_play_with_me()
        self.event_details_page.join_to_event()
        self.assertFalse(self.event_details_page.is_user_join_to_this_event())


if __name__ == "__main__":
    unittest.main(verbosity=2)
