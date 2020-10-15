"""Locators for home page"""
from selenium.webdriver.common.by import By


class HomePageLocators:
    """A class for home page locators.
    All home page locators should come here
    """

    NAV_SIGN_IN = (By.CSS_SELECTOR, 'li i.sign-in-header')
    SIGN_UP_BODY = (By.CSS_SELECTOR,
                    '#root > div > section > div > div > div.btn-group-sign > '
                    'button.btn-sign.btn-color-w.btn.btn-warning')
    SIGN_IN_BODY = (By.CSS_SELECTOR,
                    '#root > div > section > div > div > div.btn-group-sign > '
                    'button.btn-sign.btn-color-w.btn.btn-secondary')
    LEFT_SLIDE_BUTTON = (By.CSS_SELECTOR, '#home-event > div > div:nth-child(2) > div > div > '
                                          'button.slick-arrow.slick-prev')
    RIGHT_SLIDE_BUTTON = (By.CSS_SELECTOR, '#home-event > div > div:nth-child(2) > div > div > '
                                           'button.slick-arrow.slick-next')
    EVENT_DETAILS_BUTTON = (By.CSS_SELECTOR, '#event_5 > div:nth-child(4) > button')
    MORE_EVENTS_BUTTON = (By.CSS_SELECTOR,
                          '#home-event > div > div.d-flex.justify-content-end.row > a > div > button > p')
    TRAINER_ONE_BUTTON = (By.CSS_SELECTOR, '#home-trainer > div > div:nth-child(2) > div:nth-child(1) > a > '
                                           'p.trainer-name')
    TRAINER_TWO_BUTTON = (By.CSS_SELECTOR, '#home-trainer > div > div:nth-child(2) > div:nth-child(2) > a > '
                                           'p.trainer-title')
    TRAINER_THREE_BUTTON = (By.CSS_SELECTOR, '#home-trainer > div > div:nth-child(2) > div:nth-child(3) > a > '
                                             'p.trainer-title')
    TRAINER_FOUR_BUTTON = (By.CSS_SELECTOR, '#home-trainer > div > div:nth-child(2) > div:nth-child(4) > a > '
                                            'p.trainer-title')
    COURSE_PHOTO = (By.CSS_SELECTOR, '#course_3 > div > div.course-cover-photo')
    COURSE_TITLE = (By.CSS_SELECTOR, '#course_3 > div > h3')
    COURSE_RATE = (By.CSS_SELECTOR, '#course_3 > div > div.d-flex.justify-content-end.home-rate')
    COURSE_DESCRIPTION = (By.CSS_SELECTOR, '#course_3 > div > p')
    MORE_COURSES_BUTTON = (By.CSS_SELECTOR, '#home-course > div > div.d-flex.justify-content-end.row > a > div > '
                                            'button > p')
    SIGN_UP_BODY_SECOND = (By.CSS_SELECTOR, '#root > div > div.home-last-block.container > div > '
                                            'div.header-block.col-sm-7 > div > button.btn-sign.btn.btn-warning')
    SIGN_IN_BODY_SECOND = (By.CSS_SELECTOR, '#root > div > div.home-last-block.container > div > '
                                            'div.header-block.col-sm-7 > div > button.btn-sign.btn.btn-secondary')
    NAV_SIGN_IN = (By.CSS_SELECTOR, "li i.sign-in-header")
    USER_MENU_BUTTON = (By.CSS_SELECTOR, ".header-user-menu .dropdown .dropdown-button")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".dropdown-menu span")
    CREATE_COURSE_BUTTON = (By.CSS_SELECTOR, '#root > div > div > header > div > div > div.header-user-menu > '
                                             'div > div > a:nth-child(3)')
    PROFILE_ICON = (By.CSS_SELECTOR, "button img")
    CREATE_COURSE_BUTTON = (By.CSS_SELECTOR, "header.header:nth-child(1) div.container div.row div.header-user-menu"
                                             " div.dropdown.show div.dropdown-menu.dropdown-menu-right.show > "
                                             "a.dropdown-item:nth-child(3)")
