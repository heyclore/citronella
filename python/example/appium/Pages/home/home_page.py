from appium.webdriver.common.appiumby import AppiumBy
from citronella import ui


class HomePage:

    def accessibility_button(self):
        from Pages.accessibility.accessibility_page import AccessibilityPage
        return ui(AppiumBy.ACCESSIBILITY_ID, 'Accessibility', AccessibilityPage)

    def animation_button(self):
        from Pages.animation.animation_page import AnimationPage
        return ui(AppiumBy.ACCESSIBILITY_ID, 'Animation', AnimationPage)

    def app_button(self):
        from Pages.app.app_page import AppPage
        return ui(AppiumBy.ACCESSIBILITY_ID, 'App', AppPage)

    def os_button(self):
        from Pages.os.os_page import OsPage
        return ui(AppiumBy.ACCESSIBILITY_ID, 'OS', OsPage)
