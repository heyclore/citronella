from appium.webdriver.common.appiumby import AppiumBy
from citronella import ui, PlaceholderPage


class DefaultLayoutPage:
    ACTIVITY = '.animation.LayoutAnimationsByDefault'

    def add_button(self):
        return ui(AppiumBy.ACCESSIBILITY_ID, 'Add Button')
