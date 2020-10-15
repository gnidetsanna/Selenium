"""Locators for temporary email client page"""
from selenium.webdriver.common.by import By


class TemporaryEmailPageLocators:
    """A class for all temporary email client page locators"""
    COPY_EMAIL_ADDRESS_BUTTON = (By.CSS_SELECTOR, 'div.input-box-col.hidden-xs-sm > button')
    OPEN_EMAIL_BUTTON = (By.CSS_SELECTOR, 'li:nth-child(2) > div.col-box.hidden-xs-sm > span > a')
    ACTIVATION_LINK = (By.CSS_SELECTOR, 'div.inbox-data-content-intro > p:nth-child(3) > a')
    ACTIVATION_BUTTON = (By.CSS_SELECTOR, '#root > div > main > div > div > div > button')
    EMAIL_ADDRESS_FIELD = (By.CSS_SELECTOR, '#mail')
