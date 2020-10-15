from selenium.webdriver.common.by import By

"""Locators for the filter on course page"""

COURSE_FILTER_BUTTON = (By.CSS_SELECTOR, '.bm-burger-button')
FILTER_BY_MUSIC_CHECKBOX = (By.CSS_SELECTOR, '.custom-control-label[for="Music"]')
CLOSE_FILTER_WINDOW = (By.CSS_SELECTOR, '.bm-cross-button')
FIRST_COURSE_ON_PAGE = (By.CSS_SELECTOR, '#page-wrap > div > div.container > div.row > div:nth-child(1) > div > a > div')
FILTER_BY_SPORT_CHECKBOX = (By.CSS_SELECTOR, '.custom-control-label[for="Sport"]')
FILTER_BY_SOFTWARE_CHECKBOX = (By.CSS_SELECTOR, '.custom-control-label[for="Software"]')
SPORT_COURSE_CATEGORY = '//*[@id="page-wrap"]/div/div[4]/div[2]/div[1]/div/a/div/div[2]/p/p[text()="Sport"]'
SOFTWARE_COURSE_CATEGORY = '//*[@id="page-wrap"]/div/div[4]/div[2]/div[1]/div/a/div/div[2]/p/p[text()="Software"]'
MUSIC_COURSE_CATEGORY = '//*[@id="page-wrap"]/div/div[4]/div[2]/div[1]/div/a/div/div[2]/p/p[text()="Music"]'
FILTER_BY_STATUS_OPEN = (By.CSS_SELECTOR, '.custom-control-label[for="openCustomCheckbox"]')
SUBSCRIBE_BUTTON = (By.CSS_SELECTOR, '.btn-sign.btn.btn-warning')
FILTER_BY_STATUS_CLOSED = (By.CSS_SELECTOR, '.custom-control-label[for="closedCustomCheckbox"]')
OPEN_COURSE_ICON = '//*[@id="root"]/div/main/div/div[1]/div/h1/span[text()="Open"]'
CLOSED_COURSE_ICON = '//*[@id="root"]/div/main/div/div[1]/div/h1/span[text()="Closed"]'
FREE_COST_FILTER = (By.CSS_SELECTOR, '.custom-control-label[for="freeCustomRadio"]')
COURSE_COSTS_ZERO = '//*[@id="root"]/div/main/div/div[2]/div[2]/div/div[2]/span[text()="0"]'
PAID_COST_FILTER = (By.CSS_SELECTOR, '.custom-control-label[for="paidCustomRadio"]')

MUSIC_COURSE_ON_PAGE = '//*[contains(text(), "Music")]'
SPORT_COURSE_ON_PAGE = '//*[contains(text(), "Sport")]'
SOFTWARE_COURSE_ON_PAGE = '//*[contains(text(), "Software")]'
OTHER_COURSE_ON_PAGE = '//*[contains(text(), "Other")]'

TEST_COURSE = '//*[contains(text(), "Test_subscribe_course")]'
TEST_COURSE_CSS = (By.CSS_SELECTOR, '#page-wrap > div > div.container > div.row > div:nth-child(3) > div > a > div > div.event-body.card-body > div')