"""Locators for admin-dashboard page"""
from selenium.webdriver.common.by import By


class AdminDashboardPageLocators:
    """A class for all admin page locators"""
    ADMIN_DASHBOARD = (By.CSS_SELECTOR, 'div > a:nth-child(1)')
    DASHBOARD_USERS = (By.CSS_SELECTOR, 'div:nth-child(1) > a > div')
    DASHBOARD_USERS_STATUSES = (By.CSS_SELECTOR, 'div:nth-child(2) > a > div')
    DASHBOARD_ROLE_REQUESTS = (By.CSS_SELECTOR, 'div:nth-child(3) > a > div')
    DASHBOARD_LOGS = (By.CSS_SELECTOR, 'div:nth-child(4) > a > div')

    STATUS_OF_PREINSTALLED_USER = (By.CSS_SELECTOR, '#user_3 > td:nth-child(5) > div')
    ACTIVE_STATUS = (By.CSS_SELECTOR, '#user_3 > td:nth-child(5) > div > div > button:nth-child(1)')
    BANNED_STATUS = (By.CSS_SELECTOR, '#user_3 > td:nth-child(5) > div > div > button:nth-child(2)')
    MUTED_STATUS = (By.CSS_SELECTOR, '#user_3 > td:nth-child(5) > div > div > button:nth-child(3)')
    INACTIVE_STATUS = (By.CSS_SELECTOR, '#user_3 > td:nth-child(5) > div > div > button:nth-child(4)')
    APPLY_CHANGED_STATUSES_BUTTON = (By.CSS_SELECTOR, '#users-table > div.table-actions.mt-3.row > div > button')

    LOGS_TABLE = (By.CSS_SELECTOR, '#logs-table > div:nth-child(2) > div')

    TRAINERS_REQUESTS_TABLE = (By.CSS_SELECTOR, '#requests-table > div.requests-table.row > div > table > tbody')
    NEW_REQUESTS_BUTTON = (By.CSS_SELECTOR, 'div:nth-child(2) > input')
    APPROVED_REQUESTS_BUTTON = (By.CSS_SELECTOR, 'div:nth-child(3) > input')
    REJECTED_REQUESTS_BUTTON = (By.CSS_SELECTOR, 'div:nth-child(4) > input')
    ALL_REQUESTS_BUTTON = (By.CSS_SELECTOR, 'div:nth-child(5) > input')

    APPROVE_REQUEST_BUTTON = (By.CSS_SELECTOR, 'div > button.btn-yellow.btn.btn-secondary')
    REJECT_REQUEST_BUTTON = (By.CSS_SELECTOR, 'div > button.btn-grey.btn.btn-secondary')
    TEST_REQUEST_CHECKBOX = (By.CSS_SELECTOR, 'td:nth-child(1) > input[type=checkbox]')
    SUCCESSFUL_ALERT = (By.CSS_SELECTOR, 'div > div.Toastify__toast-body')

    TEST_TRAINER_STATUS = (By.CSS_SELECTOR, '#user_3 > td:nth-child(3) > input[type=checkbox]')

    ADMIN_SIDE_NAVIGATION_MENU = (By.CSS_SELECTOR, '#wrapper > div:nth-child(1) > div:nth-child(3) > div > button')
    MANAGE_USERS_SIDE_MENU = (By.CSS_SELECTOR, 'div.bm-menu-wrap > div.bm-menu > nav > li:nth-child(1) > a')
    USERS_STATUSES_SIDE_MENU = (By.CSS_SELECTOR, 'div.bm-menu-wrap > div.bm-menu > nav > li:nth-child(2) > a')
    ROLE_REQUESTS_SIDE_MENU = (By.CSS_SELECTOR, 'div.bm-menu-wrap > div.bm-menu > nav > li:nth-child(3) > a')
    LOGS_SIDE_MENU = (By.CSS_SELECTOR, 'div.bm-menu-wrap > div.bm-menu > nav > li:nth-child(4) > a')
