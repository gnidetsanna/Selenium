"""Base Page, parent class for other pages"""
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# URLs used when testing log-in functionality
BASE_URL = os.getenv("TEST_BASE_URL", "http://localhost:3001")
PROFILE_PAGE_URL = "{}/profile".format(BASE_URL)
ABOUT_PAGE_URL = '{}/about'.format(BASE_URL)
EVENTS_PAGE_URL = '{}/events/search'.format(BASE_URL)
TRAINERS_LIST_PAGE_URL = '{}/trainers'.format(BASE_URL)
COURSES_PAGE_URL = '{}/courses/search'.format(BASE_URL)
ADMIN_DASHBOARD_URL = '{}/admin'.format(BASE_URL)
MODERATOR_DASHBOARD_URL = '{}/moderator'.format(BASE_URL)
USER_SETTINGS_URL = '{}/editprofile'.format(BASE_URL)
CREATE_COURSE_URL = '{}/create-course'.format(BASE_URL)
MY_EVENTS_URL = '{}/eventcreate'.format(BASE_URL)
HELP_URL = '{}/help'.format(BASE_URL)
COURSE_DETAILS_PAGE_URL = '{}/course/detail'.format(BASE_URL)
TRAINER_PAGE_URL = '{}/trainer/page'.format(BASE_URL)
RESET_PASSWORD_PAGE_URL = "{}/reset/password".format(BASE_URL)
EVENT_CREATE_PAGE_URL = "{}/eventcreate".format(BASE_URL)

class BasePage:
    """docstring for BasePage."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def find_element_by_css(self, by_css):
        """Method for finding element on the page
        """
        return self.wait.until(EC.visibility_of_element_located(by_css))

    def presence_of_all_elements_by_css(self, by_css):
        """Method for finding all elements that match to given selector"""
        return self.wait.until(EC.presence_of_all_elements_located(by_css))

    def click_on_element_by_css(self, by_css):
        """Method for clicking on the element"""
        self.wait.until(EC.element_to_be_clickable(by_css)).click()

    def clear_text_field_by_css(self, by_css):
        """Method for clearing the text field"""
        self.wait.until(EC.visibility_of_element_located(by_css)).clear()

    def fill_in_text_field_by_css(self, by_css, text):
        """Method for filling in the text field with text"""
        self.wait.until(EC.visibility_of_element_located(by_css)
                        ).send_keys(text)

    def click_on_href_by_css(self, css):
        """Method used to click on hrefs
        example css: a[href='/editprofile']
        """
        self.driver.find_element_by_css_selector(css).click()

    def find_any_element_by_css(self, by_css):
        """Method used to find any given element
        by_css: tuple
        example: (By.CSS_SELECTOR, "div")
        """
        return self.wait.until(EC.visibility_of_any_elements_located(by_css))

    def find_element_by_xpath(self, element_xpath):
        """Method for finding element on the page"""
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, element_xpath)))

    def find_element_by_link_text(self, text):
        return self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, text)))

    def go_to_page(self, page):
        """Method fo going to the specific page"""
        self.driver.get(page)

    def click_on_element_by_xpath(self, by_xpath):
        """Method for clicking on the element"""
        self.wait.until(EC.element_to_be_clickable(by_xpath)).click()

    def click_on_element_by_link_text(self, text):
        """Method for clicking on the text element"""
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,text))).click()