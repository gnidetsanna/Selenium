from datetime import date
from pages import base_page
from locators.users_development_plan_locators import UsersDevelopmentPlanLocators as udpl
from selenium.webdriver.common.action_chains import ActionChains


RANDOM_NUMBER_FOR_NEXT_BUTTON = 20
RANDOM_TEXT_FOR_NOTE = 'Test'
MONTH_FILTER_ACTIVE = '<button type="button" class="rbc-active">Month</button>'
WEEK_FILTER_ACTIVE = '<button type="button" class="rbc-active">Week</button>'
DAY_FILTER_ACTIVE = '<button type="button" class="rbc-active">Day</button>'
SEARCH_NOTE_AFTER_DELETE = '<div class="rbc-event-content" title='\
                           + RANDOM_TEXT_FOR_NOTE + '>' + RANDOM_TEXT_FOR_NOTE + '</div>'


class UsersDevelopmentPlan(base_page.BasePage):
    """docstring for user's personal development plan page"""

    def get_current_date_from_system(self):
        """Method to get current date from system time """
        return date.today().strftime("%B %Y %d")

    def get_current_month_from_development_plan(self):
        """Method to get current date from user's personal development plan"""
        return self.find_element_by_css(udpl.CURRENT_DATE_DEVELOPMENT_PLAN).get_attribute("innerHTML")

    def get_current_date_from_development_plan(self):
        """Method to get current date from user's personal development plan"""
        today_day = self.find_element_by_css(udpl.CURRENT_DAY_DEVELOPMENT_PLAN).text
        today_m_y = self.find_element_by_css(udpl.CURRENT_DATE_DEVELOPMENT_PLAN).get_attribute("innerHTML")
        today = today_m_y + " " + today_day
        return today

    def get_current_page_stage(self):
        """Method to get stage of current page"""
        return self.driver.page_source

    def next_date_development_plan(self):
        """Method to flipping ahead user's personal development plan"""
        self.click_on_element_by_css(udpl.NEXT_DATE_DEVELOPMENT_PLAN)

    def previous_date_development_plan(self):
        """Method to flipping back user's personal development plan"""
        self.click_on_element_by_css(udpl.BACK_DATE_DEVELOPMENT_PLAN)

    def today_date_development_plan(self):
        """Method to flipping user's personal development plan to the today's date"""
        self.click_on_element_by_css(udpl.TODAY_DATE_DEVELOPMENT_PLAN)

    def week_filter_development_plan(self):
        """Method to filter user's personal development plan by week"""
        self.click_on_element_by_css(udpl.WEEK_FILTER_DEVELOPMENT_PLAN)

    def day_filter_development_plan(self):
        """Method to filter user's personal development plan by day"""
        self.click_on_element_by_css(udpl.DAY_FILTER_DEVELOPMENT_PLAN)

    def month_filter_development_plan(self):
        """Method to filter user's personal development plan by month"""
        self.click_on_element_by_css(udpl.MONTH_FILTER_DEVELOPMENT_PLAN)

    def create_new_note_today(self):
        """Method to create new note by today in user's personal development plan"""
        self.click_on_element_by_css(udpl.CREATE_NEW_NOTE_TODAY)

    def fill_title(self):
        """Method for filling in note's title text field"""
        self.clear_text_field_by_css(udpl.TITLE_OF_NOTE_FIELD)
        self.fill_in_text_field_by_css(udpl.TITLE_OF_NOTE_FIELD, RANDOM_TEXT_FOR_NOTE)

    def fill_description(self):
        """Method for filling in note's description text field"""
        self.clear_text_field_by_css(udpl.DESCRIPTION_OF_NOTE_FIELD)
        self.fill_in_text_field_by_css(udpl.DESCRIPTION_OF_NOTE_FIELD, RANDOM_TEXT_FOR_NOTE)

    def confirm_note_creation(self):
        """Method to confirm new note creation"""
        self.click_on_element_by_css(udpl.CONFIRM_CREATE_NOTE_BUTTON)

    def check_new_note_created(self):
        """Method to check if new note has been created"""
        self.find_element_by_css(udpl.CREATED_NOTE)

    def open_new_note(self):
        """Method to open created note details"""
        self.click_on_element_by_css(udpl.CREATED_NOTE)

    def delete_new_note(self):
        """Method to delete created note
        We move mouse for hide ajax-popup with note details """
        self.click_on_element_by_css(udpl.DELETE_NOTE_BUTTON)
        ActionChains(self.driver).move_by_offset(0, 50).perform()
