import unittest
from selenium import webdriver
from pages import base_page
from pages import admin_dashboard_page as adp
from pages import login_page
from pages import edit_profile_page as epp


class AdminFunctionality(unittest.TestCase):
    """Test administrator functions workability """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = login_page.LoginPage(self.driver)
        self.admin_dashboard = adp.AdminDashboardPage(self.driver)
        self.base_page = base_page.BasePage(self.driver)
        self.edit_profile_page = epp.EditProfilePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_ban_possibility(self):
        """Test possibility to ban user as administrator """
        self.login_page.sign_in_as(**login_page.ADMIN_DATA)
        self.base_page.go_to_page(base_page.ADMIN_DASHBOARD_URL)
        self.admin_dashboard.open_menu_section(adp.ADMIN_USERS_STATUSES)
        self.admin_dashboard.change_user_status_to(adp.BANNED_STATUS)
        self.admin_dashboard.apply_changed_status()
        self.assertEqual(
            self.admin_dashboard.get_name_of_selected_status(), adp.BANNED_STATUS,
            msg="Impossible to ban user")

    def test_mute_possibility(self):
        """Test possibility to mute user as administrator """
        self.login_page.sign_in_as(**login_page.ADMIN_DATA)
        self.base_page.go_to_page(base_page.ADMIN_DASHBOARD_URL)
        self.admin_dashboard.open_menu_section(adp.ADMIN_USERS_STATUSES)
        self.admin_dashboard.change_user_status_to(adp.MUTED_STATUS)
        self.admin_dashboard.apply_changed_status()
        self.assertEqual(
            self.admin_dashboard.get_name_of_selected_status(), adp.MUTED_STATUS,
            msg="Impossible to mute user")

    def test_deactivate_possibility(self):
        """Test possibility to deactivate user as administrator """
        self.login_page.sign_in_as(**login_page.ADMIN_DATA)
        self.base_page.go_to_page(base_page.ADMIN_DASHBOARD_URL)
        self.admin_dashboard.open_menu_section(adp.ADMIN_USERS_STATUSES)
        self.admin_dashboard.change_user_status_to(adp.INACTIVE_STATUS)
        self.admin_dashboard.apply_changed_status()
        self.assertEqual(
            self.admin_dashboard.get_name_of_selected_status(), adp.INACTIVE_STATUS,
            msg="Impossible to deactivate user")

    def test_reactivate_possibility(self):
        """Test possibility to reactivate user as administrator """
        self.login_page.sign_in_as(**login_page.ADMIN_DATA)
        self.base_page.go_to_page(base_page.ADMIN_DASHBOARD_URL)
        self.admin_dashboard.open_menu_section(adp.ADMIN_USERS_STATUSES)
        self.admin_dashboard.change_user_status_to(adp.ACTIVE_STATUS)
        self.admin_dashboard.apply_changed_status()
        self.assertEqual(
            self.admin_dashboard.get_name_of_selected_status(), adp.ACTIVE_STATUS,
            msg="Impossible to reactivate user")

    def test_logs_are_not_recorded(self):
        """Negative testing to ensure that logs aren't recorded"""
        self.login_page.sign_in_as(**login_page.ADMIN_DATA)
        self.base_page.go_to_page(base_page.ADMIN_DASHBOARD_URL)
        self.admin_dashboard.open_menu_section(adp.ADMIN_LOGS)
        self.assertEqual(
            self.admin_dashboard.get_logs_table_content(), adp.EMPTY_LOGS_MSG,
            msg="Logs table isn't empty")

    def test_trainers_requests_filter_by_approved(self):
        """Test possibility to filter requests by approved from trainers as administrator """
        self.login_page.sign_in_as(**login_page.ADMIN_DATA)
        self.base_page.go_to_page(base_page.ADMIN_DASHBOARD_URL)
        self.admin_dashboard.open_menu_section(adp.ADMIN_ROLE_REQUESTS)
        last_page_state = self.admin_dashboard.get_current_page_stage()
        self.admin_dashboard.change_requests_filter_criterion(adp.FILTER_REQUESTS_BY_APPROVED)
        self.assertNotEqual(
            last_page_state, self.admin_dashboard.get_current_page_stage(),
            msg="Impossible to filter requests by approved")

    def test_trainers_requests_filter_by_rejected(self):
        """Test possibility to filter requests by rejected from trainers as administrator """
        self.login_page.sign_in_as(**login_page.ADMIN_DATA)
        self.base_page.go_to_page(base_page.ADMIN_DASHBOARD_URL)
        self.admin_dashboard.open_menu_section(adp.ADMIN_ROLE_REQUESTS)
        last_page_state = self.admin_dashboard.get_current_page_stage()
        self.admin_dashboard.change_requests_filter_criterion(adp.FILTER_REQUESTS_BY_REJECTED)
        self.assertNotEqual(
            last_page_state, self.admin_dashboard.get_current_page_stage(),
            msg="Impossible to filter requests by rejecter")

    def test_trainers_requests_filter_by_all(self):
        """Test possibility to filter requests 'by all' from trainers as administrator """
        self.login_page.sign_in_as(**login_page.ADMIN_DATA)
        self.base_page.go_to_page(base_page.ADMIN_DASHBOARD_URL)
        self.admin_dashboard.open_menu_section(adp.ADMIN_ROLE_REQUESTS)
        last_page_state = self.admin_dashboard.get_current_page_stage()
        self.admin_dashboard.change_requests_filter_criterion(adp.FILTER_REQUESTS_BY_ALL)
        self.assertNotEqual(
            last_page_state, self.admin_dashboard.get_current_page_stage(),
            msg="Impossible to filter requests by all")

    def test_trainers_requests_filter_by_new(self):
        """Test possibility to filter requests by new from trainers as administrator
        first change filter to other to ensure, because 'new' filter is preinstalled """
        self.login_page.sign_in_as(**login_page.ADMIN_DATA)
        self.base_page.go_to_page(base_page.ADMIN_DASHBOARD_URL)
        self.admin_dashboard.open_menu_section(adp.ADMIN_ROLE_REQUESTS)
        self.admin_dashboard.change_requests_filter_criterion(adp.FILTER_REQUESTS_BY_APPROVED)
        last_page_state = self.admin_dashboard.get_current_page_stage()
        self.admin_dashboard.change_requests_filter_criterion(adp.FILTER_REQUESTS_BY_NEW)
        self.assertNotEqual(
            last_page_state, self.admin_dashboard.get_current_page_stage(),
            msg="Impossible to filter requests by new")

    def test_approve_trainer_request(self):
        """Test possibility to approve requests from trainers as administrator """
        self.login_page.sign_in_as(**login_page.VALID_DATA)
        self.base_page.go_to_page(base_page.USER_SETTINGS_URL)
        self.edit_profile_page.send_request_to_become_trainer()
        self.login_page.sign_out()
        self.login_page.sign_in_as(**login_page.ADMIN_DATA)
        self.base_page.go_to_page(base_page.ADMIN_DASHBOARD_URL)
        self.admin_dashboard.open_menu_section(adp.ADMIN_ROLE_REQUESTS)
        self.admin_dashboard.select_request_from_trainer()
        self.admin_dashboard.approve_selected_request()
        self.admin_dashboard.change_menu_of_dashboard_to(adp.ADMIN_USERS)
        self.assertTrue(
            self.admin_dashboard.is_test_trainer_status_activated(),
            msg="Impossible to approve the request")

    def test_reject_trainer_request(self):
        """Test possibility to reject requests from trainers as administrator """
        self.login_page.sign_in_as(**login_page.VALID_DATA)
        self.base_page.go_to_page(base_page.USER_SETTINGS_URL)
        self.edit_profile_page.send_request_to_become_trainer()
        self.login_page.sign_out()
        self.login_page.sign_in_as(**login_page.ADMIN_DATA)
        self.base_page.go_to_page(base_page.ADMIN_DASHBOARD_URL)
        self.admin_dashboard.open_menu_section(adp.ADMIN_ROLE_REQUESTS)
        self.admin_dashboard.select_request_from_trainer()
        self.admin_dashboard.reject_selected_request()
        self.admin_dashboard.change_menu_of_dashboard_to(adp.ADMIN_USERS)
        self.assertFalse(
            self.admin_dashboard.is_test_trainer_status_activated(),
            msg="Reject-function worked incorrectly")


if __name__ == "__main__":
    unittest.main(verbosity=2)
