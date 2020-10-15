from pages import base_page
from locators.admin_dashboard_locators import AdminDashboardPageLocators as adpl

ADMIN_USERS = "{}/users".format(base_page.ADMIN_DASHBOARD_URL)
ADMIN_USERS_STATUSES = "{}/statuses".format(base_page.ADMIN_DASHBOARD_URL)
ADMIN_ROLE_REQUESTS = '{}/roles'.format(base_page.ADMIN_DASHBOARD_URL)
ADMIN_LOGS = '{}/logs'.format(base_page.ADMIN_DASHBOARD_URL)

BANNED_STATUS = 'Banned'
MUTED_STATUS = 'Muted'
INACTIVE_STATUS = 'Idle'
ACTIVE_STATUS = 'Active'

EMPTY_LOGS_MSG = 'Logs will be here'

FILTER_REQUESTS_BY_APPROVED = 'Approved'
FILTER_REQUESTS_BY_REJECTED = 'Rejected'
FILTER_REQUESTS_BY_ALL = 'All'
FILTER_REQUESTS_BY_NEW = 'New'


class AdminDashboardPage(base_page.BasePage):
    """docstring for AdminDashboardPage"""

    def open_menu_section(self, url):
        """Method to open the specified submenu of dashboard"""
        if url == ADMIN_USERS:
            self.click_on_element_by_css(adpl.DASHBOARD_USERS)
        elif url == ADMIN_USERS_STATUSES:
            self.click_on_element_by_css(adpl.DASHBOARD_USERS_STATUSES)
        elif url == ADMIN_ROLE_REQUESTS:
            self.click_on_element_by_css(adpl.DASHBOARD_ROLE_REQUESTS)
        elif url == ADMIN_LOGS:
            self.click_on_element_by_css(adpl.DASHBOARD_LOGS)
        self.wait.until(base_page.EC.url_to_be(url))

    def change_user_status_to(self, status):
        """Method to change user status to specific"""
        self.click_on_element_by_css(adpl.STATUS_OF_PREINSTALLED_USER)
        if status == ACTIVE_STATUS:
            self.click_on_element_by_css(adpl.ACTIVE_STATUS)
        elif status == BANNED_STATUS:
            self.click_on_element_by_css(adpl.BANNED_STATUS)
        elif status == MUTED_STATUS:
            self.click_on_element_by_css(adpl.MUTED_STATUS)
        elif status == INACTIVE_STATUS:
            self.click_on_element_by_css(adpl.INACTIVE_STATUS)

    def get_name_of_selected_status(self):
        """Method to get name of selected status from field"""
        return self.find_element_by_css(adpl.STATUS_OF_PREINSTALLED_USER).text

    def apply_changed_status(self):
        """Method to apply user status change"""
        self.click_on_element_by_css(adpl.APPLY_CHANGED_STATUSES_BUTTON)

    def get_logs_table_content(self):
        """Method to get contents from the logs table"""
        return self.find_element_by_css(adpl.LOGS_TABLE).text

    def change_requests_filter_criterion(self, criterion):
        """Method to change filter criterion for requests to specific"""
        if criterion == FILTER_REQUESTS_BY_APPROVED:
            self.click_on_element_by_css(adpl.APPROVED_REQUESTS_BUTTON)
        elif criterion == FILTER_REQUESTS_BY_REJECTED:
            self.click_on_element_by_css(adpl.REJECTED_REQUESTS_BUTTON)
        elif criterion == FILTER_REQUESTS_BY_ALL:
            self.click_on_element_by_css(adpl.ALL_REQUESTS_BUTTON)
        elif criterion == FILTER_REQUESTS_BY_NEW:
            self.click_on_element_by_css(adpl.NEW_REQUESTS_BUTTON)
        self.wait.until(base_page.EC.presence_of_element_located(adpl.TRAINERS_REQUESTS_TABLE))

    def select_request_from_trainer(self):
        """Method to select request from test-trainer """
        self.click_on_element_by_css(adpl.TEST_REQUEST_CHECKBOX)

    def approve_selected_request(self):
        """Method to approve selected request from trainer"""
        self.click_on_element_by_css(adpl.APPROVE_REQUEST_BUTTON)
        self.find_element_by_css(adpl.SUCCESSFUL_ALERT)

    def reject_selected_request(self):
        """Method to reject selected request from trainer"""
        self.click_on_element_by_css(adpl.REJECT_REQUEST_BUTTON)
        self.find_element_by_css(adpl.SUCCESSFUL_ALERT)

    def open_admin_side_menu(self):
        """Method to open admin side navigation menu"""
        self.click_on_element_by_css(adpl.ADMIN_SIDE_NAVIGATION_MENU)

    def change_menu_of_dashboard_to(self, url):
        """Method to change menu of administrator dashboard to specified"""
        self.open_admin_side_menu()
        if url == ADMIN_USERS:
            self.click_on_element_by_css(adpl.MANAGE_USERS_SIDE_MENU)
        elif url == ADMIN_USERS_STATUSES:
            self.click_on_element_by_css(adpl.USERS_STATUSES_SIDE_MENU)
        elif url == ADMIN_ROLE_REQUESTS:
            self.click_on_element_by_css(adpl.ROLE_REQUESTS_SIDE_MENU)
        elif url == ADMIN_LOGS:
            self.click_on_element_by_css(adpl.LOGS_SIDE_MENU)
        self.wait.until(base_page.EC.url_to_be(url))

    def is_test_trainer_status_activated(self):
        """Method to ensure that trainer-function successfully applied"""
        return self.find_element_by_css(adpl.TEST_TRAINER_STATUS).is_selected()

    def get_current_page_stage(self):
        """Method to get stage of current page"""
        return self.driver.page_source
