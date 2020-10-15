"""Locators for the courses page."""
from selenium.webdriver.common.by import By


class CoursesPageLocators:
    """A class for courses page locators.
    All locators from the course page should come here.
    """

    SEARCH_ICON = (By.CSS_SELECTOR, '#search')
    SMALL_SEARCH_ICON = (By.CSS_SELECTOR, '#search_submit')
    COURSE_HEADER = (By.CSS_SELECTOR, '.event-header.card-header')
    COURSE_DESCRIPTION_CARD = (By.CSS_SELECTOR, '#page-wrap > div > div.container > div.row > div:nth-child(1) > div '
                                                '> a > div')
    COURSE_TITLE_IN_CARD = (By.CSS_SELECTOR, '.event-body.card-body')
    COURSE_DESCRIPTION_DETAILS_TEXT = (By.CSS_SELECTOR, '.card-text')
    COURSE_FOOTER = (By.CSS_SELECTOR, '.card-event-footer.card-footer')

