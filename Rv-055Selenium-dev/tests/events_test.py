import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages import events_page as ep
from pages import base_page


class Events(unittest.TestCase):
    """Docstring for Events."""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.events_page = ep.EventsPage(self.driver)
        self.base_page = base_page.BasePage(self.driver)
        self.events_page.go_to()

    def tearDown(self):
        self.driver.quit()

    def test_events_header(self):
        self.assertEqual("Events", self.events_page.check_page_header().text)

    def test_events_button(self):
        self.driver.get(base_page.ABOUT_PAGE_URL)
        self.assertTrue(self.events_page.click_on_event_button())

    def test_next_navigation_button(self):
        self.assertTrue(self.events_page.click_on_next_button())
        self.assertEqual("2", self.events_page.get_actual_navi_page())

    def test_prev_navigation_button(self):
        self.events_page.click_on_next_button()
        self.events_page.click_on_prev_button()
        self.assertEqual("1", self.events_page.get_actual_navi_page())

    def test_event_filter_other(self):
        self.events_page.go_to()
        self.events_page.click_on_filter_button()
        self.events_page.click_on_other_filter()
        self.events_page.close_filter()
        self.driver.implicitly_wait(40)
        self.assertEqual("Category: Other", self.events_page.get_category_from_event().text)

    def test_event_filter_sport(self):
        self.events_page.go_to()
        self.events_page.click_on_filter_button()
        self.events_page.click_on_sport_filter()
        self.events_page.close_filter()
        self.driver.implicitly_wait(40)
        self.assertEqual("Category: Sport", self.events_page.get_category_from_event().text)

    def test_event_filter_music(self):
        self.events_page.go_to()
        self.events_page.click_on_filter_button()
        self.events_page.click_on_music_filter()
        self.events_page.close_filter()
        self.driver.implicitly_wait(40)
        self.assertEqual("Category: Music", self.events_page.get_category_from_event().text)

    def test_event_filter_software(self):
        self.events_page.go_to()
        self.events_page.click_on_filter_button()
        self.events_page.click_on_software_filter()
        self.events_page.close_filter()
        self.driver.implicitly_wait(40)
        self.assertEqual("Category: Software", self.events_page.get_category_from_event().text)

    def test_events_sort_by_asc(self):
        self.driver.implicitly_wait(40)
        date_before_filtering = self.events_page.get_event_date()
        self.events_page.sort_by_asc()
        self.assertEqual(date_before_filtering, self.events_page.get_event_date())

    def test_events_sort_by_desc(self):
        self.driver.implicitly_wait(40)
        date_before_filtering = self.events_page.get_event_date()
        self.events_page.sort_by_desc()
        self.assertEqual(date_before_filtering, self.events_page.get_event_date())


if __name__ == "__main__":
    unittest.main(verbosity=2)
