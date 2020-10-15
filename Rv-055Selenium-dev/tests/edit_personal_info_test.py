"""test case to check the possibility to edit personal info"""
import unittest
from selenium import webdriver
from pages import login_page as lp
from pages import profile_page as pp
from pages import base_page
from pages import edit_profile_page as epp

New = {"Name": "Vasya", "Surname": "Pupkin", "Login": "Ololo"}
Old = {}

class edit_personal_info(unittest.TestCase):
    """edit personal info"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.login_page = lp.LoginPage(self.driver)
        self.profile_page = pp.ProfilePage(self.driver)
        self.editprofile_page = epp.EditProfilePage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_edit_name_user(self):
        self.login_page.sign_in_as(**lp.VALID_DATA)
        Old["Name"] = self.profile_page.check_name()
        self.editprofile_page.go_to()
        self.editprofile_page.change_name(New["Name"])
        self.profile_page.go_to()
        self.assertTrue(self.profile_page.check_name()==New['Name'])
        self.editprofile_page.go_to()
        self.editprofile_page.change_name(Old["Name"])

    def test_edit_surname_user(self):
        self.login_page.sign_in_as(**lp.VALID_DATA)
        Old["Surname"] = self.profile_page.check_surname()
        self.editprofile_page.go_to()
        self.editprofile_page.change_surname(New["Surname"])
        self.profile_page.go_to()
        self.assertTrue(self.profile_page.check_surname()==New['Surname'])
        self.editprofile_page.go_to()
        self.editprofile_page.change_surname(Old["Surname"])

    def test_edit_login_user(self):
        self.login_page.sign_in_as(**lp.VALID_DATA)
        Old["Login"] = self.profile_page.check_login()
        self.editprofile_page.go_to()
        self.editprofile_page.change_login(New["Login"])
        self.profile_page.go_to()
        self.assertTrue(self.profile_page.check_login()==New['Login'])
        self.editprofile_page.go_to()
        self.editprofile_page.change_login(Old["Login"])

    def test_edit_name_trainer(self):
        self.login_page.sign_in_as(**lp.TRAINER_DATA)
        Old["Name"] = self.profile_page.check_name()
        self.editprofile_page.go_to()
        self.editprofile_page.change_name(New["Name"])
        self.profile_page.go_to()
        self.assertTrue(self.profile_page.check_name()==New['Name'])
        self.editprofile_page.go_to()
        self.editprofile_page.change_name(Old["Name"])

    def test_edit_surname_trainer(self):
        self.login_page.sign_in_as(**lp.TRAINER_DATA)
        Old["Surname"] = self.profile_page.check_surname()
        self.editprofile_page.go_to()
        self.editprofile_page.change_surname(New["Surname"])
        self.profile_page.go_to()
        self.assertTrue(self.profile_page.check_surname()==New['Surname'])
        self.editprofile_page.go_to()
        self.editprofile_page.change_surname(Old["Surname"])

    def test_edit_login_trainer(self):
        self.login_page.sign_in_as(**lp.TRAINER_DATA)
        Old["Login"] = self.profile_page.check_login()
        self.editprofile_page.go_to()
        self.editprofile_page.change_login(New["Login"])
        self.profile_page.go_to()
        self.assertTrue(self.profile_page.check_login()==New['Login'])
        self.editprofile_page.go_to()
        self.editprofile_page.change_login(Old["Login"])

    def test_edit_name_moderator(self):
        self.login_page.sign_in_as(**lp.MODERATOR_DATA)
        Old["Name"] = self.profile_page.check_name()
        self.editprofile_page.go_to()
        self.editprofile_page.change_name(New["Name"])
        self.profile_page.go_to()
        self.assertTrue(self.profile_page.check_name()==New['Name'])
        self.editprofile_page.go_to()
        self.editprofile_page.change_name(Old["Name"])

    def test_edit_surname_moderator(self):
        self.login_page.sign_in_as(**lp.MODERATOR_DATA)
        Old["Surname"] = self.profile_page.check_surname()
        self.editprofile_page.go_to()
        self.editprofile_page.change_surname(New["Surname"])
        self.profile_page.go_to()
        self.assertTrue(self.profile_page.check_surname()==New['Surname'])
        self.editprofile_page.go_to()
        self.editprofile_page.change_surname(Old["Surname"])

    def test_edit_login_moderator(self):
        self.login_page.sign_in_as(**lp.MODERATOR_DATA)
        Old["Login"] = self.profile_page.check_login()
        self.editprofile_page.go_to()
        self.editprofile_page.change_login(New["Login"])
        self.profile_page.go_to()
        self.assertTrue(self.profile_page.check_login()==New['Login'])
        self.editprofile_page.go_to()
        self.editprofile_page.change_login(Old["Login"])

    def test_edit_name_admin(self):
        self.login_page.sign_in_as(**lp.ADMIN_DATA)
        Old["Name"] = self.profile_page.check_name()
        self.editprofile_page.go_to()
        self.editprofile_page.change_name(New["Name"])
        self.profile_page.go_to()
        self.assertTrue(self.profile_page.check_name()==New['Name'])
        self.editprofile_page.go_to()
        self.editprofile_page.change_name(Old["Name"])

    def test_edit_surname_admin(self):
        self.login_page.sign_in_as(**lp.ADMIN_DATA)
        Old["Surname"] = self.profile_page.check_surname()
        self.editprofile_page.go_to()
        self.editprofile_page.change_surname(New["Surname"])
        self.profile_page.go_to()
        self.assertTrue(self.profile_page.check_surname()==New['Surname'])
        self.editprofile_page.go_to()
        self.editprofile_page.change_surname(Old["Surname"])

    def test_edit_login_admin(self):
        self.login_page.sign_in_as(**lp.ADMIN_DATA)
        Old["Login"] = self.profile_page.check_login()
        self.editprofile_page.go_to()
        self.editprofile_page.change_login(New["Login"])
        self.profile_page.go_to()
        self.assertTrue(self.profile_page.check_login()==New['Login'])
        self.editprofile_page.go_to()
        self.editprofile_page.change_login(Old["Login"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
