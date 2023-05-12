class ContentsPage:

    def home_page(self):
        #from Pages.home.home_page import HomePage
        return HomePage

    def gallery_page(self):
        #from Pages.accessibility.accessibility_page import AccessibilityPage
        return GalleryPage

    def navigation_menu(self):
        #from Pages.animation.animation_page import AnimationPage
        return NavigationMenu


from appium.webdriver.common.appiumby import AppiumBy
from citronella import ui

class NavigationMenu:

    def home_button(self):
        return ui(AppiumBy.ACCESSIBILITY_ID, 'Home\nTab 1 of 2')

    def gallery_button(self):
        return ui(AppiumBy.ACCESSIBILITY_ID, 'Gallery\nTab 2 of 2')

class HomePage(ContentsPage().navigation_menu()):
    pass

class GalleryPage(ContentsPage().navigation_menu()):

    def add_button(self):
        return ui(AppiumBy.ACCESSIBILITY_ID, 'Add')

    def text_input(self):
        return ui(AppiumBy.CLASS_NAME, 'android.widget.EditText')

    def text_lists(self):
        return ui(AppiumBy.XPATH, '//android.view.View[@content-desc="Item*"]')
