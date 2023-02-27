from appium.webdriver.common.appiumby import AppiumBy
from citronella import ui, PlaceholderPage


class EventsPage:
    ACTIVITY = '.animation.AnimatorEvents'

    def play_button(self):
        return ui(AppiumBy.ACCESSIBILITY_ID, 'Play')

    def cancel_button(self):
        return ui(AppiumBy.ACCESSIBILITY_ID, 'Cancel')
