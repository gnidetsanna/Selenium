"""Locators for profile page"""
from selenium.webdriver.common.by import By


class ProfilePageLocators:
    """A class for profile page locators.
    All profile page locators should come here
    """
    PROFILE_INFO_CSS = (By.CSS_SELECTOR, "div .profile-info")
    MAIN_PROFILE_ICON_CSS = (
        By.CSS_SELECTOR, "div[class='edit-label'] a[href='/editprofile']")
    INPUT_NEWPASS_CSS = (By.CSS_SELECTOR, "input[name='new_password']")
    INPUT_RENEWPASS_CSS = (By.CSS_SELECTOR, "input[name='re_new_password']")
    BRUSH_EDIT_TOOL_CSS = (By.CSS_SELECTOR, "a[title='Edit profile']")
    CHANGE_PASS_BTN = (By.CSS_SELECTOR, ".btn-warning")
    EDIT_LABEL_CSS = (By.CSS_SELECTOR, "div .edit-tool")
    EDITPROFILE_BUTTON = (By.CSS_SELECTOR, "div:nth-child(2) > a > img")
    NAME = (By.CSS_SELECTOR, "div.user-name > div:nth-child(1) > h2:nth-child(1)")
    SURNAME = (By.CSS_SELECTOR, "div.user-name > div:nth-child(1) > h2:nth-child(2)")
    LOGIN = (By.CSS_SELECTOR, 'div.profile-info.col > div.user-info > h6')
    PHONE_CSS = (By.CSS_SELECTOR, "div.tab-content > div.tab-pane.active > div.contact-info.row > div:nth-child(2)")
    ADRESS_CSS = (By.CSS_SELECTOR, "div.tab-content > div.tab-pane.active > div:nth-child(4) > div:nth-child(2)")
    FAVOURIVE_COURSES_SHOW_CSS = (By.CSS_SELECTOR, "div.show-hide span")
    COURSE_CSS = (By.CSS_SELECTOR, ".wrap-manage-course")
    TEACHER_OWN_COURSES = (By.CSS_SELECTOR, 'div:nth-child(1) > span')
    MY_OWN_COURSES = (By.CSS_SELECTOR,'div.event-and-courses.align > div:nth-child(1) > span')
    CREATED_EVENTS = (By.CSS_SELECTOR, "li:nth-child(9) > a > div > span")
    PERSONAL_DEVELOPMENT_PLAN = (By.CSS_SELECTOR, 'div.user-courses.tab-item')
    FOLLOWING_COURSES = (By.CSS_SELECTOR,
                         'div.event-and-courses.align > li:nth-child(4) > a > div')
    UNSUBSCRIBE_COURSE_BUTTON_IN_PROFILE = (By.CSS_SELECTOR,
                                            '#root > div > div:nth-child(3) > div > div:nth-child(1) > div >'
                                            'div:nth-child(3) > div.tab-content > div.tab-pane.active > div >'
                                            'div > div.row > div > div > div > div > div:nth-child(3)')

