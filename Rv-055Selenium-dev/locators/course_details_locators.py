"""Locators for course details page."""

from selenium.webdriver.common.by import By


class CourseDetailsLocators:
    """A class for course details page locators.
    All locators should come here.
    """
    COURSE_HEADER = (By.CSS_SELECTOR,
                     '#page-wrap > div > div.container > div.row > div:nth-child(1) > div > a > div > '
                     'div.event-header.card-header')
    COURSE_BODY = (By.CSS_SELECTOR,
                   '#page-wrap > div > div.container > div.row > div:nth-child(1) > div > a > div > '
                   'div.event-body.card-body')
    COURSE_FOOTER = (By.CSS_SELECTOR,
                     '#page-wrap > div > div.container > div.row > div:nth-child(1) > div > a > div > '
                     'div.card-event-footer.card-footer')
    COURSE_DETAILS_HEADER = (By.CSS_SELECTOR, '#root > div > main > div > div.cd-header > div > h1')
    SHORT_COURSE_INFO = (By.CSS_SELECTOR, '#root > div > main > div > div:nth-child(2) > div.cd-info-block')
    ABOUT_COURSE = (By.CSS_SELECTOR, '#root > div > main > div > div.container > div:nth-child(1) > '
                                     'div.course-detail-first-col.col-12.col-md-6')
    CALENDAR = (By.CSS_SELECTOR, '#root > div > main > div > div.container > div:nth-child(1) > '
                                 'div.course-detail-second-col.col-12.col-md-6 > div > div > div.DayPicker-Months')
    COMMENT_SECTION = (By.CSS_SELECTOR, '#root > div > main > div > div.container > div:nth-child(2) > '
                                        'div.pt-3.border-right.col-md-4 > form > div:nth-child(2) > textarea')
    SUBSCRIBE_BUTTON = (By.CSS_SELECTOR, '.btn-sign.btn.btn-warning')
    BACK_BUTTON = (By.CSS_SELECTOR, '#root > div > main > div > div.container > '
                                    'div.btn-group-course-detail.d-flex.justify-content-between.row > '
                                    'div.d-flex.flex-wrap.col-md-12.col-lg-8 > a > button')
    UNSUBSCRIBE_MESSAGE = (By.CSS_SELECTOR, 'body > div:nth-child(7) > div > div > div > div.Toastify__toast-body')
    COMMENT_BUTTON = (By.CSS_SELECTOR, '#root > div > main > div > div.container > div:nth-child(2) > '
                                       'div.pt-3.border-right.col-md-4 > form > div:nth-child(3) > button')
    FIRST_COMMENT = (By.CSS_SELECTOR, '#root > div > main > div > div.container > div:nth-child(2) > '
                                      'div.pt-3.bg-white.col > div > div:nth-child(3) > div')



