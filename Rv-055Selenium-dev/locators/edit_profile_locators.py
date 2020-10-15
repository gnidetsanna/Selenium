"""Locators for edit profile page"""
from selenium.webdriver.common.by import By



class EditProfilePageLocators:
    """A class for 'edit profile' page locators.
    All profile page locators should come here
    """
    EDIT_PROFILE_AVATAR_CSS = (By.CSS_SELECTOR, "div .edit-avatar")
    CHOOSE_FILE_BUTTON_CSS = (By.CSS_SELECTOR, "div .button-avatar-input")
    UPLOAD_IMAGE_CSS = (By.CSS_SELECTOR, "div .button-avatar")
    SAVE_ALL_CSS = (By.CSS_SELECTOR, "div .button-saveall.btn.btn-secondary.btn-lg.btn-block")
    SAVE_ALL_BUTTON = (By.CSS_SELECTOR, 'div.col-4 > button')
    NAME_FIELD = (By.CSS_SELECTOR, 'div:nth-child(1) > input:nth-child(7)')
    SURNAME_FIELD = (By.CSS_SELECTOR, 'div:nth-child(1) > input:nth-child(9)')
    LOGIN_FIELD = (By.CSS_SELECTOR, 'div:nth-child(1) > input:nth-child(5)')
    LOCATION_FIELD_CSS = (By.CSS_SELECTOR, "div .location-search-input")
    CONTACT_FIELD_CSS = (By.CSS_SELECTOR, "div:nth-child(1) > input:nth-child(15)")
    WANT_TO_BECOME_TRAINER_BUTTON = (By.CSS_SELECTOR, 'div.top-text-2.fill-edit-collumn.col-sm-12.col-md-6 > button')
    BECOME_TRAINER_BUTTON = (By.CSS_SELECTOR, "div.container form.form-group div.row div.top-text-2.fill-edit-collumn."
                                              "col-sm-12.col-md-6 > button.text-button-trainer.btn.btn-secondary.btn-lg"
                                              ".btn-block:nth-child(10)")
