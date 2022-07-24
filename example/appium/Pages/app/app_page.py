from appium.webdriver.common.appiumby import AppiumBy
from citronella import Ui, PlaceholderPage


class AppPage:

    def action_bar_button(self):
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Action Bar', PlaceholderPage)

    def activity_button(self):
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Activity', PlaceholderPage)

    def alarm_button(self):
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Alarm', PlaceholderPage)
