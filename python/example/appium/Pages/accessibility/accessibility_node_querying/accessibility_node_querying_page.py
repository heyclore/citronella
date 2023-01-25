from appium.webdriver.common.appiumby import AppiumBy
from citronella import Ui


class AccessibilityNodeQueryingPage:
    ACTIVITY = '.accessibility.TaskListActivity'

    def take_out_trash_checkbox(self):
        return Ui(AppiumBy.XPATH,
                '//android.widget.TextView[contains(@content-desc, '
                '"Trash")]/following-sibling::android.widget.CheckBox')
