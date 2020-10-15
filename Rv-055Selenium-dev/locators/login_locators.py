"""Locators for login page"""
from selenium.webdriver.common.by import By


class LoginPageLocators:
    """A class for login page locators.
    All login page locators should come here
    """
    LOGIN_FORM = (By.ID, 'login-form')
    INPUT_FIELD_MAIL_CSS = (By.ID, 'email')
    INPUT_FIELD_PASS_CSS = (By.ID, 'password')
    CONFIRM_SIGN_IN_BUTTON_CSS = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOT_PASSWORD_CSS = (By.CSS_SELECTOR, "div a[href='/reset/password']")
    RESET_PASS_FORM_CSS = (By.CSS_SELECTOR, ".reset-pass-form")
    BUTTON_RESET_PASS_CSS = (By.CSS_SELECTOR, "button.reset-pass-form")
    INPUT_NEW_PASSWORD_CSS = (By.CSS_SELECTOR, "input[name='new_password']")
    INPUT_RE_NEW_PASSWORD_CSS = (By.CSS_SELECTOR, "input[name='re_new_password']")
