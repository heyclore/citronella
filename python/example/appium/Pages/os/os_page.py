from appium.webdriver.common.appiumby import AppiumBy
from citronella import Ui

class MorseCodePage:

    def morse_input(self):
        return Ui(AppiumBy.ID, 'io.appium.android.apis:id/text')

    def vibrate_button(self):
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Vibrate')

class OsPage:

    def morse_code_button(self):
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Morse Code', MorseCodePage)
