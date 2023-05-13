from appium.webdriver.common.appiumby import AppiumBy
from citronella import ui
from Pages.contents_page import ContentsPage


class HomePage(ContentsPage().navigation_menu()):
    pass
