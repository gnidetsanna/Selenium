import unittest
from selenium import webdriver
from pages import base_page
from pages import temporary_email_page as tep
from pages import registration_page as reg_p
from pages import login_page as lp
from pages import profile_page as pp


class UsersSignUP(unittest.TestCase):
    """Test sign-up possibility into system"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(base_page.BASE_URL)
        self.main_window = self.driver.window_handles[0]
        self.driver.execute_script('window.open("{}");'.format(tep.TEMPORARY_EMAIL_CLIENT))
        self.email_window = self.driver.window_handles[1]
        self.sign_up_window = reg_p.RegistationPage(self.driver)
        self.email_service = tep.TemporaryEmailPage(self.driver)
        self.login_window = lp.LoginPage(self.driver)
        self.profile_window = pp.ProfilePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_registration_as_user(self):
        """test sign-up possibility as the user """
        self.driver.switch_to.window(self.email_window)
        self.email_service.get_temporary_email()
        self.driver.switch_to.window(self.main_window)
        self.sign_up_window.open_sign_up_window()
        self.sign_up_window.fill_in_email_field()
        self.sign_up_window.fill_in_password_fields()
        self.sign_up_window.confirm_sign_up()
        self.driver.switch_to.window(self.email_window)
        self.email_service.open_email()
        self.email_service.activate_account()
        data_for_sing_in = self.sign_up_window.create_dictionary_for_login()
        self.login_window.sign_in_as(**data_for_sing_in)
        self.assertTrue(
            self.profile_window.is_profile_info_present(),
            msg="User hasn't been successfully created, profile not available")

    def test_registration_as_teacher(self):
        """test sign-up possibility as the teacher """
        self.driver.switch_to.window(self.email_window)
        self.email_service.get_temporary_email()
        self.driver.switch_to.window(self.main_window)
        self.sign_up_window.open_sign_up_window()
        self.sign_up_window.mark_as_teacher()
        self.sign_up_window.fill_in_email_field()
        self.sign_up_window.fill_in_password_fields()
        self.sign_up_window.confirm_sign_up()
        self.driver.switch_to.window(self.email_window)
        self.email_service.open_email()
        self.email_service.activate_account()
        data_for_sing_in = self.sign_up_window.create_dictionary_for_login()
        self.login_window.sign_in_as(**data_for_sing_in)
        self.assertTrue(
            self.sign_up_window.is_teacher_functions_have_applied(),
            msg="Teacher-functions haven't been applied")


if __name__ == "__main__":
    unittest.main(verbosity=2)
