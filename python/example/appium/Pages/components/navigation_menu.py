from appium.webdriver.common.appiumby import AppiumBy
from citronella import ui

class NavigationMenu:

    def home_button(self):
        return ui(AppiumBy.ACCESSIBILITY_ID, 'Home\nTab 1 of 2')

    def gallery_button(self):
        return ui(AppiumBy.ACCESSIBILITY_ID, 'Gallery\nTab 2 of 2')
