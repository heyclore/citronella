from appium.webdriver.common.appiumby import AppiumBy
from citronella import ui
from Pages.contents_page import ContentsPage


class GalleryPage(ContentsPage().navigation_menu()):

    def add_button(self):
        return ui(AppiumBy.ACCESSIBILITY_ID, 'Add')

    def text_input(self):
        return ui(AppiumBy.CLASS_NAME, 'android.widget.EditText')

    def text_lists(self):
        return ui(AppiumBy.XPATH, '//android.view.View[@content-desc="Item*"]')
