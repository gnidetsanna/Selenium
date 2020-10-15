"""Locators for registration page"""
from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    """A class for all registration page locators"""
    INPUT_FIELD_EMAIL_REG = (By.CSS_SELECTOR, '#email')
    INPUT_FIELD_PASS_REG = (By.CSS_SELECTOR, '#password')
    INPUT_FIELD_CONFIRM_PASS_REG = (By.CSS_SELECTOR, '#confirmpass')
    CONFIRM_SIGN_UP_BUTTON = (By.CSS_SELECTOR, 'div.col-md-8 > button')
    TEACHER_MARK = (By.CSS_SELECTOR, '#userteacher')
    TEACHER_OWN_COURSES = (By.CSS_SELECTOR, 'div.tab-item.user-courses')
