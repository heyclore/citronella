from appium.webdriver.common.appiumby import AppiumBy
from citronella import ui, PlaceholderPage


class CustomEvaluatorPage:
    ACTIVITY = '.animation.CustomEvaluator'

    def play_button(self):
        return ui(AppiumBy.ACCESSIBILITY_ID, 'Play')
