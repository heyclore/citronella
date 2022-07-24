from appium.webdriver.common.appiumby import AppiumBy
from citronella import Ui, PlaceholderPage


class DefaultLayoutPage:
    ACTIVITY = '.animation.LayoutAnimationsByDefault'

    def add_button(self):
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Add Button')
