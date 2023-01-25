from appium.webdriver.common.appiumby import AppiumBy
from citronella import Ui, PlaceholderPage


class CloningPage:
    ACTIVITY = '.animation.AnimationCloning'

    def run_button(self):
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Run')
