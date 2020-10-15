"""Locators for event edit page"""
from selenium.webdriver.common.by import By


class EventEditLocators:
    """A class for event edit page locators.
    All profile page locators should come here
    """
    EVENT_NAME_FIELD = (By.CSS_SELECTOR,
        "div:nth-child(1) > div.col-sm-10.col-md-10 > input")
    EVENT_CATEGORY = (By.CSS_SELECTOR,
        "div.column-dropdown-button.col-sm-4.col-md-4 > select")
    EVENT_CATEGORY_OTHER = (By.CSS_SELECTOR,
        "div.column-dropdown-button.col-sm-4.col-md-4 > select >option:nth-child(2)")
    EVENT_DESCRIPTION_FIELD = (By.CSS_SELECTOR,
        "div > main > form > div > div > div:nth-child(2) > div > textarea")
    LOCATION_FIELD = (By.CSS_SELECTOR,
        "div:nth-child(3) > div.col-md-4.offset-md-1 > div > div > input")
    CHOOSE_FILE_BUTTON_CSS = (By.CSS_SELECTOR,
        "#root > div > main > form > div > div > div:nth-child(4) > div > div > form > input")
    UPLOAD_IMAGE_CSS = (By.CSS_SELECTOR,
        "form > div > div > div:nth-child(4) > div > div > form > button")
    SAVE_ALL_CSS = (By.CSS_SELECTOR,
        "#root > div > main > form > div > div > div:nth-child(6) > div > div:nth-child(2) > button")
