import unittest
from selenium import webdriver

from pages import login_page as lp
from pages import edit_profile_page as ep
from pages import profile_page as pp


class TrainerEditProfile(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = lp.LoginPage(self.driver)
        self.edit_profile_page = ep.EditProfilePage(self.driver)
        self.profile_page = pp.ProfilePage(self.driver)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_trainer_change_icon(self):
        """Test ability to check if authorized trainer of the system have
        the possibility to change profile icon"""
        self.login_page.sign_in_as(**lp.TRAINER_DATA)
        self.profile_page.click_on_edit_profile_button()
        self.edit_profile_page.click_on_change_icon_button()
        self.edit_profile_page.click_on_choose_file_button()
        self.edit_profile_page.upload_file_button()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.edit_profile_page.click_on_save_all_button()
        self.assertTrue(self.edit_profile_page.check_image())

    def test_user_change_icon(self):
        """Test ability to check if authorized user of the system have
        the possibility to change profile icon"""
        self.login_page.sign_in_as(**lp.VALID_DATA)
        self.profile_page.click_on_edit_profile_button()
        self.edit_profile_page.click_on_change_icon_button()
        self.edit_profile_page.click_on_choose_file_button()
        self.edit_profile_page.upload_file_button()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.edit_profile_page.click_on_save_all_button()
        self.assertTrue(self.edit_profile_page.check_image())



    def test_trainer_change_contact_info(self):
        """Test ability to check if authorized trainer of the system have
                the possibility to change contact information"""
        New_info = {"Address": "Paris", "Phone": "9084563"}
        self.login_page.sign_in_as(**lp.TRAINER_DATA)
        self.profile_page.click_on_edit_profile_button()
        self.edit_profile_page.trainer_change_location(New_info['Address'])
        self.edit_profile_page.trainer_change_phone(New_info['Phone'])
        self.edit_profile_page.click_on_save_all_button()
        self.profile_page.go_to()
        self.driver.implicitly_wait(30)
        self.assertTrue(self.profile_page.check_location() == New_info['Address'])
        self.assertTrue(self.profile_page.check_phone() == New_info['Phone'])


    def test_trainer_change_contact_info(self):
        """Test ability to check if authorized trainer of the system have
                the possibility to change contact information"""
        New_info = {"Address": "Paris", "Phone": "9084563"}
        self.login_page.sign_in_as(**lp.TRAINER_DATA)
        self.profile_page.click_on_edit_profile_button()
        self.edit_profile_page.change_location(New_info['Address'])
        self.edit_profile_page.change_phone(New_info['Phone'])
        self.edit_profile_page.click_on_save_all_button()
        self.profile_page.go_to()
        self.driver.implicitly_wait(30)
        self.assertTrue(self.profile_page.check_location() == New_info['Address'])
        self.assertTrue(self.profile_page.check_phone() == New_info['Phone'])

def test_user_change_contact_info(self):
        """Test ability to check if authorized user of the system have
                the possibility to change contact information"""
        New_info = {"Address": "Paris", "Phone": "9084563"}
        self.login_page.sign_in_as(**lp.VALID_DATA)
        self.profile_page.click_on_edit_profile_button()
        self.edit_profile_page.change_location(New_info['Address'])
        self.edit_profile_page.change_phone(New_info['Phone'])
        self.edit_profile_page.click_on_save_all_button()
        self.profile_page.go_to()
        self.driver.implicitly_wait(30)
        self.assertTrue(self.profile_page.check_location() == New_info['Address'])
        self.assertTrue(self.profile_page.check_phone() == New_info['Phone'])

if __name__ == "__main__":
    unittest.main(verbosity=2)
