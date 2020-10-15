"""Class for the Profile page with methods which are used for testing"""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.command import Command
from pages import base_page
from pages.base_page import BasePage
from locators.profile_locators import ProfilePageLocators as ppl
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class ProfilePage(BasePage):
    """Class with methods used to test Profile page"""

    def go_to(self):
        """Method for redirecting to profile page"""
        self.driver.get(base_page.PROFILE_PAGE_URL)

    def is_profile_info_present(self):
        """Method to check if profile info present"""
        try:
            self.find_element_by_css(ppl.PROFILE_INFO_CSS)
            return True
        except TimeoutException:
            return False

    def click_on_brush_icon(self):
        """Method to click on brush icon inside profile page"""
        self.click_on_element_by_css(ppl.BRUSH_EDIT_TOOL_CSS)

    def fill_in_new_password(self, new_pass):
        """fill in new password on editprofile"""
        self.fill_in_text_field_by_css(ppl.INPUT_NEWPASS_CSS,
                                       new_pass)
        self.fill_in_text_field_by_css(ppl.INPUT_RENEWPASS_CSS,
                                       new_pass)

    def click_on_profile_href(self):
        """Method to click on profile href"""
        self.click_on_href_by_css(ppl.MAIN_PROFILE_ICON_CSS[1])

    def click_change_password(self):
        """click on change password on editprofile"""
        self.click_on_element_by_css(ppl.CHANGE_PASS_BTN)

    def get_storage_item(self, **kwargs):
        """Method returs value of storage item
        example input:
        key='token'
        """
        return self.driver.execute(Command.GET_LOCAL_STORAGE_ITEM, kwargs)

    def click_on_edit_profile_button(self):
        """Method used to click on 'edit profile'
        button
        """
        self.click_on_element_by_css(ppl.EDIT_LABEL_CSS)

    def check_name(self):
        """Metod to check name"""
        return (self.find_element_by_css(ppl.NAME).text)

    def check_surname(self):
        """Metod to check surname"""
        return (self.find_element_by_css(ppl.SURNAME).text)

    def check_login(self):
        """Metod to check login"""
        return (self.find_element_by_css(ppl.LOGIN).text)

    def check_location(self):
        """Method to check changed location"""
        return self.find_element_by_css(ppl.ADRESS_CSS).text

    def check_phone(self):
        """Method to check changed phone"""
        return self.find_element_by_css(ppl.PHONE_CSS).text

    def click_on_show_fav_courses(self):
        """Method to click on Show your favourite courses"""
        self.click_on_element_by_css(ppl.FAVOURIVE_COURSES_SHOW_CSS)

    def click_on_own_courses(self):
        """Method used to click on own courses"""
        self.click_on_element_by_css(ppl.TEACHER_OWN_COURSES)

    def is_courses_present(self):
        """Method used to find all own courses"""
        try:
            self.find_any_element_by_css(ppl.COURSE_CSS)
            return True
        except TimeoutException:
            return False

    def make_course_buttons_visible(self):
        """Method used to make course buttons visible, in profile"""
        self.driver.execute_script(
            """document.querySelector(
                "li.tab-item div.user-courses-profile div").click()
            let element = document.querySelector(
                "div.event-card-wrap div.manage-buttons-wrap");
            element.style.display="flex";
            """)

    def click_on_on_unsubscribe_btn(self):
        """Method used to click on unsubscribe btn"""
        self.driver.execute_script("""document.querySelector(
          "div.event-card-wrap div.buttons-wrap-inner :nth-child(3)").click()
          """)

    def go_to_created_evets(self):
        """Method used to click on created events"""
        self.click_on_element_by_css(ppl.CREATED_EVENTS)

    def go_to_development_plan(self):
        """Method to enter to the user's personal development plan """
        self.click_on_element_by_css(ppl.PERSONAL_DEVELOPMENT_PLAN)

    def click_on_following_courses(self):
        """Method for clicking of following courses in profile"""
        self.click_on_element_by_css(ppl.FOLLOWING_COURSES)

    def unsubscribe_from_course_in_profile(self):
        """Method for unsubscribing from courses in profile"""
        self.go_to()
        self.click_on_following_courses()
        self.action = ActionChains(self.driver)
        self.menu = self.find_element_by_link_text('Test_subscribe_course')
        self.action.move_to_element(self.menu).perform()
        self.click_on_element_by_css(ppl.UNSUBSCRIBE_COURSE_BUTTON_IN_PROFILE)
