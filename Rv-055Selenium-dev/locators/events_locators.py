"""Locators for events page"""
from selenium.webdriver.common.by import By


class EventsPageLocators:
    """A class for events page locators.
    All events page locators should come here
    """
    HEADER_TEXT_CLASS_NAME = "title-events"
    EVENT_NFS_HEADER = (By.CSS_SELECTOR,
                        "div.container div.container:nth-child(4) div.row div.wrap-manage-course.col-sm-12.col-md-6.col-lg-4:nth-child(4) div.event-card-wrap a.card-link div.event-card.card div.event-body.card-body div.event-card-header.card-title > a:nth-child(1)")
    EVENT_SEARCH_BUTTON = (By.CSS_SELECTOR, "#search")
    EVENT_SEARCH_SUBMIT = (By.CSS_SELECTOR, "#search-submit")
    EVENT_HEADER = (By.CSS_SELECTOR,
                    "div.container div.container:nth-child(4) div.row div.wrap-manage-course.col-sm-12.col-md-6.col-lg-4:nth-child(1) div.event-card-wrap a.card-link div.event-card.card div.event-body.card-body div.event-card-header.card-title > a:nth-child(1)")
    EVENT_DETAILS_TEXT = (By.CSS_SELECTOR,
                          "div.home-event div.container:nth-child(2) div.row:nth-child(1) div.course-detail-first-col.col > p.main-text")
    EVENT_DETAILS_PERSON = (By.CSS_SELECTOR,
                            "div.home-event div.ed-info-block:nth-child(2) div.d-flex.flex-wrap.container div.ed.cd-trainer:nth-child(1) span.main-text > a:nth-child(1)")
    EVENT_DETAILS_LOCATION = (By.CSS_SELECTOR,
                              "div.home-event div:nth-child(1) div.ed-info-block:nth-child(2) div.d-flex.flex-wrap.container div.ed.cd-loc:nth-child(2) > span.main-text.cd-loc")
    EVENT_DETAILS_DATE = (By.CSS_SELECTOR,
                          "div.home-event div:nth-child(1) div.ed-info-block:nth-child(2) div.d-flex.flex-wrap.container div.ed.cd-date:nth-child(3) > span.main-text.cd-date")
    EVENT_BUTTON_IN_HEADER = (By.CSS_SELECTOR, "a.nav-link[href='/events/search'][activeclass='active']")
    NAVI_NEXT_BUTTON = (By.CSS_SELECTOR, "a.cdp_i[href='#!+1']")
    NAVI_PREV_BUTTON = (By.CSS_SELECTOR, "a.cdp_i[href='#!-1']")
    NAVI_ACTUAL_PAGE = (By.CSS_SELECTOR, "div.content_detail__pagination.cdp")
    SEARCH = (By.CSS_SELECTOR, '#search')
    NO_EVENTS_MESSAGE = (By.CSS_SELECTOR,
                         "#page-wrap > div > div.container > div.row > div > h2")
    FILTER_BUTTON = (By.CSS_SELECTOR, ".bm-burger-button button")
    FILTER_CATEGORY_OTHER = (By.CSS_SELECTOR, "label.custom-control-label[for='Other']")
    FILTER_CATEGORY_SPORT = (By.CSS_SELECTOR, "label.custom-control-label[for='Sport']")
    FILTER_CATEGORY_MUSIC = (By.CSS_SELECTOR, "label.custom-control-label[for='Music']")
    FILTER_CATEGORY_SOFTWARE = (By.CSS_SELECTOR, "label.custom-control-label[for='Software']")
    CLOSE_FILTER_BUTTON = (By.CSS_SELECTOR, ".bm-cross-button button")
    EVENT_CARD_CATEGORY = (By.CSS_SELECTOR, "p.card-text p")
    EVENT_SORT_BY = (By.CSS_SELECTOR, "select[name='select']")
    EVENT_CARD_DATE = (By.CSS_SELECTOR, "div.event-header.card-header")
    COMMENT_FIELD = (By.CSS_SELECTOR, "form textarea")
    LEAVE_COMMENT_BUTTON = (By.CSS_SELECTOR, "form button")
    FIRST_COMMENT_USER_NAME = (By.CSS_SELECTOR, "div.comment div h6")
    FIRST_COMMENT_TEXT = (By.CSS_SELECTOR, "div.comment div")
    ALL_COMMENTS_SELECTOR = (By.CSS_SELECTOR, "div#root div.comment")
    WHO_PLAY_WITH_ME = (By.CSS_SELECTOR,
                        "#page-wrap > div > div.container > div.row > div:nth-child(2) > div > a > div > div.event-body.card-body > div > a")
    JOIN_TO_EVENT = (By.CSS_SELECTOR, "div.d-flex.flex-wrap.col-md-12.col-lg-8 > button")
    FIRST_EVENT_CARD = (By.CSS_SELECTOR, "#page-wrap > div > div.container > div.row > div:nth-child(1)")
    EVENT_DETAILS_TITLE = (By.CSS_SELECTOR, "#root > div > main > div > div:nth-child(1) > div:nth-child(1) > div > div > h1")
    EVENT_DETAILS_COMMENT_LIST = (By.CSS_SELECTOR, "div.home-event div.container:nth-child(2) div.row:nth-child(2)"
                                                   " div.pt-3.bg-white.col:nth-child(2) > div.commentList")
