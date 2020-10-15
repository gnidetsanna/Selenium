import unittest
from selenium import webdriver
from pages import base_page
from pages import login_page
from pages import profile_page
from pages import users_development_plan_page as udpp


class UsersDevelopmentPlanPage(unittest.TestCase):
    """Test user's personal development plan workability """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_page = base_page.BasePage(self.driver)
        self.login_page = login_page.LoginPage(self.driver)
        self.profile_page = profile_page.ProfilePage(self.driver)
        self.development_plan_page = udpp.UsersDevelopmentPlan(self.driver)
        self.login_page.sign_in_as(**login_page.VALID_DATA)
        self.profile_page.go_to_development_plan()

    def tearDown(self):
        self.driver.quit()

    def test_correct_calendar_current_date(self):
        """Test for correct determination of the current date  """
        today_from_system_time = self.development_plan_page.get_current_date_from_system()
        today_from_development_plan = self.development_plan_page.get_current_date_from_development_plan()
        self.assertEqual(
            today_from_system_time, today_from_development_plan,
            msg="Incorrect current date in the personal development plan")

    def test_calendar_back_next_buttons(self):
        """Test workability of Test next and back calendar buttons """
        current_month = self.development_plan_page.get_current_month_from_development_plan()
        self.development_plan_page.next_date_development_plan()
        self.development_plan_page.previous_date_development_plan()
        self.development_plan_page.previous_date_development_plan()
        self.development_plan_page.next_date_development_plan()
        self.assertTrue(
            current_month in self.development_plan_page.get_current_page_stage(),
            msg="Incorrect next/back-buttons work")

    def test_calendar_today_buttons(self):
        """Test workability of today calendar button """
        current_month = self.development_plan_page.get_current_month_from_development_plan()
        for _ in range(udpp.RANDOM_NUMBER_FOR_NEXT_BUTTON):
            self.development_plan_page.next_date_development_plan()
        self.development_plan_page.today_date_development_plan()
        self.assertTrue(
            current_month in self.development_plan_page.get_current_page_stage(),
            msg="Incorrect today-button work")

    def test_calendar_week_filter(self):
        """Test possibility to filter calendar data by week """
        self.development_plan_page.week_filter_development_plan()
        self.assertTrue(
            udpp.WEEK_FILTER_ACTIVE in self.development_plan_page.get_current_page_stage(),
            msg="Filtering works wrong")

    def test_calendar_day_filter(self):
        """Test possibility to filter calendar data by day """
        self.development_plan_page.day_filter_development_plan()
        self.assertTrue(
            udpp.DAY_FILTER_ACTIVE in self.development_plan_page.get_current_page_stage(),
            msg="Filtering works wrong")

    def test_calendar_month_filter(self):
        """Test possibility to filter calendar data by month
        first change filter to other to ensure, because filter by month is preinstalled """
        self.development_plan_page.week_filter_development_plan()
        self.development_plan_page.month_filter_development_plan()
        self.assertTrue(
            udpp.MONTH_FILTER_ACTIVE in self.development_plan_page.get_current_page_stage(),
            msg="Filtering works wrong")

    def test_creation_new_note(self):
        """Test possibility to create new note """
        self.development_plan_page.create_new_note_today()
        self.development_plan_page.fill_title()
        self.development_plan_page.fill_description()
        self.development_plan_page.confirm_note_creation()
        self.assertTrue(self.development_plan_page.check_new_note_created,
                        msg="Note wasn't created")

    def test_delete_created_note(self):
        """Test possibility to delete created note """
        self.development_plan_page.create_new_note_today()
        self.development_plan_page.fill_title()
        self.development_plan_page.fill_description()
        self.development_plan_page.confirm_note_creation()
        self.development_plan_page.open_new_note()
        self.development_plan_page.delete_new_note()
        self.assertFalse(
            udpp.SEARCH_NOTE_AFTER_DELETE in self.development_plan_page.get_current_page_stage(),
            msg="Note wasn't deleted")


if __name__ == "__main__":
    unittest.main(verbosity=2)
