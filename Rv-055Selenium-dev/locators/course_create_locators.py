"""Locators for Create Course page."""

from selenium.webdriver.common.by import By


class NewCourseLocators:
    """A class for new course page locators.
    All locators should come here.
    """

    COURSE_NAME_BUTTON = (By.CSS_SELECTOR, '#root > div > main > form > '
                                           'div > div.cd-header > div > h1 > input')

    ABOUT_BUTTON = (By.CSS_SELECTOR, '#root > div > main > form > div > div.container >'
                                     ' div > div.course-detail-first-col.col-12.col-md-6 > textarea')

    PHOTO_BUTTON = (By.CSS_SELECTOR, 'form input[type="file"]')

    MEMBERS_BUTTON = (By.CSS_SELECTOR, '#root > div > main > form > div > div.container > div > '
                                       'div.course-detail-first-col.col-12.col-md-6 > '
                                       'input.field-courselimit.form-control')

    DURATION_BUTTON = (By.CSS_SELECTOR, '#root > div > main > form > div > div.container > div > '
                                        'div.course-detail-first-col.col-12.col-md-6 > input:nth-child(8)')

    START_DAY_BUTTON = (By.CSS_SELECTOR, '#root > div > main > form > div > div.container > div > '
                                         'div.course-detail-first-col.col-12.col-md-6 > input:nth-child(10)')

    START_TIME_BUTTON = (By.CSS_SELECTOR, '#root > div > main > form > div > div.container > div > '
                                          'div.course-detail-first-col.col-12.col-md-6 > input:nth-child(12)')

    PRICE_BUTTON = (By.CSS_SELECTOR, '#root > div > main > form > div > div.container > div > '
                                     'div.course-detail-first-col.col-12.col-md-6 > input:nth-child(14)')

    LOCATION_BUTTON = (By.CSS_SELECTOR, '#root > div > main > form > div > div.container > div > '
                                        ' div.course-detail-first-col.col-12.col-md-6 > div > div > input')

    OPTION_BUTTON = (By.CSS_SELECTOR, 'div.course-detail-first-col.col-12.col-md-6 > select:nth-child(20) > '
                                      'option:nth-child(3)')

    CREATE_COURSE_BUTTON = (By.CSS_SELECTOR, 'div.course-detail-first-col.col-12.col-md-6 > button')

