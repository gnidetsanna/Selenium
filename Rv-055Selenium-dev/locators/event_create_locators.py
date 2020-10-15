"""Locators for event ceate page"""
from selenium.webdriver.common.by import By


class EventCreateLocators:
    """A class for event create page locators.
    All profile page locators should come here
    """
    CREATE_VENT = (By.CSS_SELECTOR,
    'div.col-8.offset-2.col-sm-8.offset-sm-2.col-md-6.offset-md-3 > a > button')
