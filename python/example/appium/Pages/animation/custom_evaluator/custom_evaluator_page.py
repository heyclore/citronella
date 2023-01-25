from appium.webdriver.common.appiumby import AppiumBy
from citronella import Ui, PlaceholderPage


class CustomEvaluatorPage:
    ACTIVITY = '.animation.CustomEvaluator'

    def play_button(self):
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Play')
