import unittest

from selenium import webdriver


from pages import courses_page as cp


"""Test cases for Black Box testing 'Filter courses' """

class CourseFilterTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.course_page = cp.CoursesPage(self.driver)
        self.course_page.go_to_CourseSearchPage()
        self.course_page.click_on_filter_course_button()


    def tearDown(self):
        self.driver.quit()

    def test_filter_by_music(self):

        """ After selecting music category by filter only music courses should be left"""

        self.course_page.click_on_filter_music_checkbox()
        self.course_page.close_filter_window()
        self.assertTrue(self.course_page.is_first_course_on_page_of_music_category(),
                        msg = 'Filter by music doesn"t work')


    def test_filter_by_sport(self):

        """ After selecting music category by filter only sport courses should be left"""

        self.course_page.click_on_filter_sport_checkbox()
        self.course_page.close_filter_window()
        self.assertTrue(self.course_page.is_first_course_on_page_of_sport_category(),
                        msg='Filter by sport doesn"t work')

    def test_filter_by_sport_and_music(self):

        """ After selecting music and sport category by filter only sport and music courses should be left"""
        self.course_page.click_on_filter_sport_checkbox()
        self.course_page.click_on_filter_music_checkbox()
        self.course_page.close_filter_window()
        self.driver.implicitly_wait(2)
        self.assertTrue(self.course_page.is_course_on_page_of_sport_category(),
                        msg = 'No sport courses')
        self.assertTrue(self.course_page.is_course_on_page_of_music_category(),
                        msg = 'No music courses')
        self.assertFalse(self.course_page.is_course_on_page_of_software_category(),
                         msg = 'Software courses are present on page')
        self.assertFalse(self.course_page.is_course_on_page_of_other_category(),
                         msg = 'Other courses are present on page')

    def test_filter_by_software(self):

        """ After selecting music category by filter only software courses should be left"""

        self.course_page.click_on_filter_software_checkbox()
        self.course_page.close_filter_window()
        self.assertTrue(self.course_page.is_first_course_on_page_of_software_category(),
                        msg='Filter by software doesn"t work')

    def test_filter_by_status_open(self):

        """ After selecting open course status by filter only opened courses should be left"""
        self.course_page.click_on_filter_status_open()
        self.course_page.close_filter_window()
        self.course_page.click_on_first_course_on_page()
        self.assertTrue(self.course_page.is_subscribe_button_present_in_course_page(),
                        msg='Element is not found')
        self.assertTrue(self.course_page.is_open_icon_present_in_course_page(),
                        msg = 'Open icon hasn"t been found')

    def test_filter_by_status_closed(self):

        """ After selecting closed course status by filter only closed courses should be left"""
        self.course_page.click_on_filter_status_closed()
        self.course_page.close_filter_window()
        self.course_page.click_on_first_course_on_page()
        self.assertFalse(self.course_page.is_subscribe_button_present_in_course_page(),
                        msg='Subscribe button is present')
        self.assertTrue(self.course_page.is_closed_icon_present_in_course_page(),
                        msg = 'Closed icon hasn"t been found')

    def test_filter_by_cost_free(self):

        """ After selecting free cost by filter only free courses should be left"""
        self.course_page.click_on_filter_cost_free()
        self.course_page.close_filter_window()
        self.course_page.click_on_first_course_on_page()
        self.assertTrue(self.course_page.is_the_course_free(),
                        msg = 'Course isn"t free')

    def test_filter_by_paid_cost(self):

        """ After selecting paid cost by filter only paid courses should be left"""
        self.course_page.click_on_filter_cost_paid()
        self.course_page.close_filter_window()
        self.course_page.click_on_first_course_on_page()
        self.assertFalse(self.course_page.is_the_course_free(),
                        msg = 'Course is free')

if __name__ == "__main__":
    unittest.main(verbosity=2)