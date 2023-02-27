from appium.webdriver.common.appiumby import AppiumBy
from citronella import ui, PlaceholderPage


class AppPage:

    def action_bar_button(self):
        return ui(AppiumBy.ACCESSIBILITY_ID, 'Action Bar', PlaceholderPage)

    def activity_button(self):
        return ui(AppiumBy.ACCESSIBILITY_ID, 'Activity', PlaceholderPage)

    def alarm_button(self):
        return ui(AppiumBy.ACCESSIBILITY_ID, 'Alarm', PlaceholderPage)
