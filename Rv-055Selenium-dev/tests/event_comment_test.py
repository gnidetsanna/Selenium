"""As the user of the system I want to have the possibility
to leave comment to the event #24"""

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages import login_page as lp
from pages import profile_page as pp
from pages import events_page as ep
from pages import base_page
from helpers.query_comment import query_db

class EventComment(unittest.TestCase):
    """As the user of the system I want to have the possibility
    to leave comment to the event #24"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.login_page = lp.LoginPage(self.driver)
        self.profile_page = pp.ProfilePage(self.driver)
        self.events_page = ep.EventsPage(self.driver)
        self.events_page.wait = WebDriverWait(self.driver, 3)

    def tearDown(self):
        self.driver.quit()

    def test_leave_comment_as_authorized_user(self):
        """Verify authorized users can leave the comment #115"""
        self.login_page.sign_in_as(**lp.VALID_DATA)
        self.login_page.is_page_loaded(base_page.PROFILE_PAGE_URL)
        self.events_page.click_on_event_button()
        self.events_page.click_on_event()
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        comment = self.events_page.write_a_comment()
        self.events_page.leave_comment()
        self.driver.refresh()
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        comment_element = self.events_page.find_comment()
        self.assertIn(comment, comment_element.text, msg="comment not found")

    def test_leave_comment_as_unauthorized_user(self):
        """Verify unauthorized users can't leave the comment #116"""
        self.events_page.go_to()
        self.events_page.click_on_event()
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        self.assertFalse(self.events_page.is_comment_textarea_present(),
                         msg="comment field was found")

    def test_validate_user_input(self):
        """User input validation test in event comment field #117"""
        self.login_page.sign_in_as(**lp.VALID_DATA)
        self.login_page.is_page_loaded(base_page.PROFILE_PAGE_URL)
        self.events_page.click_on_event_button()
        self.events_page.click_on_event()
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        comment = "'',4,5); SELECT SLEEP(50); --"
        self.events_page.write_a_comment(comment)
        self.events_page.leave_comment()
        db_comment = query_db()[0]['comment']
        self.assertEqual(comment, db_comment, msg="sanitize your inputs")


if __name__ == "__main__":
    unittest.main()
