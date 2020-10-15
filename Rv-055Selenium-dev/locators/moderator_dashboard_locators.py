"""Locators for moderator dashboard"""
from selenium.webdriver.common.by import By

class ModeratorDashboardLocators:

    MODERATOR_DASHBOARD = (By.CSS_SELECTOR, "header.header:nth-child(1) div.container div.row "
                                                   "div.header-user-menu div.dropdown.show div.dropdown-menu."
                                                   "dropdown-menu-right.show > a.dropdown-item:nth-child(1)")
    ROLE_REQUESTS = (By.CSS_SELECTOR, "div.container div.dashboard-menu.row div.pb-3.col-md-6:nth-child(3)"
                                      " a:nth-child(1) div:nth-child(1) > div:nth-child(1)")
    MANAGE_USERS = (By.CSS_SELECTOR, "div.container div.dashboard-menu.row div.pb-3.col-md-6:nth-child(1) "
                                     "a:nth-child(1) div:nth-child(1) > div:nth-child(1)")
    CHECK_BOX = (By.CSS_SELECTOR, "div.container div.row:nth-child(2) div.col-md-10 div.admin-tables"
                                  " div.requests-table.row div.requests-table-wrap.col table:nth-child(1) "
                                  "tbody:nth-child(2) tr:nth-child(1) td:nth-child(1) > input:nth-child(1)")
    APPROVE_BUTTON = (By.CSS_SELECTOR, "div.container div.row:nth-child(2) div.col-md-10 div.admin-tables "
                                       "div.table-actions.mt-3.row div.col > button.btn-yellow.btn."
                                       "btn-secondary:nth-child(3)")