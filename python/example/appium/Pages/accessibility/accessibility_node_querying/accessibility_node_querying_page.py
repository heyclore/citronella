from appium.webdriver.common.appiumby import AppiumBy
from citronella import ui


class AccessibilityNodeQueryingPage:
    ACTIVITY = '.accessibility.TaskListActivity'

    def take_out_trash_checkbox(self):
        return ui(AppiumBy.XPATH,
                '//android.widget.TextView[contains(@content-desc, '
                '"Trash")]/following-sibling::android.widget.CheckBox')
