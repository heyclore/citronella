from appium.webdriver.common.appiumby import AppiumBy
from citronella import ui, PlaceholderPage


class CloningPage:
    ACTIVITY = '.animation.AnimationCloning'

    def run_button(self):
        return ui(AppiumBy.ACCESSIBILITY_ID, 'Run')
