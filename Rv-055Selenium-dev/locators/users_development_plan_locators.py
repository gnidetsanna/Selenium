"""Locators for user's personal development plan page"""
from selenium.webdriver.common.by import By


class UsersDevelopmentPlanLocators:
    """A class for all user's personal development plan page locators"""
    PERSONAL_DEVELOPMENT_PLAN = (By.CSS_SELECTOR, 'div.user-courses.tab-item')
    CURRENT_DAY_DEVELOPMENT_PLAN = (By.CSS_SELECTOR, 'div.rbc-date-cell.rbc-now.rbc-current > a')
    CURRENT_DATE_DEVELOPMENT_PLAN = (By.CSS_SELECTOR, 'span.rbc-toolbar-label')
    TODAY_DATE_DEVELOPMENT_PLAN = (By.CSS_SELECTOR, 'div.rbc-toolbar > span:nth-child(1) > button:nth-child(1)')
    BACK_DATE_DEVELOPMENT_PLAN = (By.CSS_SELECTOR, 'div.rbc-toolbar > span:nth-child(1) > button:nth-child(2)')
    NEXT_DATE_DEVELOPMENT_PLAN = (By.CSS_SELECTOR, 'div.rbc-toolbar > span:nth-child(1) > button:nth-child(3)')
    MONTH_FILTER_DEVELOPMENT_PLAN = (By.CSS_SELECTOR, 'div.rbc-toolbar > span:nth-child(3) > button:nth-child(1')
    WEEK_FILTER_DEVELOPMENT_PLAN = (By.CSS_SELECTOR, 'div.rbc-toolbar > span:nth-child(3) > button:nth-child(2)')
    DAY_FILTER_DEVELOPMENT_PLAN = (By.CSS_SELECTOR, 'div.rbc-toolbar > span:nth-child(3) > button:nth-child(3)')
    CREATE_NEW_NOTE_TODAY = (By.CSS_SELECTOR, 'div.rbc-row-bg > div.rbc-day-bg.rbc-today')
    TITLE_OF_NOTE_FIELD = (By.CSS_SELECTOR, '#pdp-own-event-title')
    DESCRIPTION_OF_NOTE_FIELD = (By.CSS_SELECTOR, '#pdp-own-event-desc')
    CONFIRM_CREATE_NOTE_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-warning')
    CREATED_NOTE = (By.CSS_SELECTOR, 'div.rbc-event-content')
    DELETE_NOTE_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-danger')
