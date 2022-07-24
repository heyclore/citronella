from appium.webdriver.common.appiumby import AppiumBy
from citronella import Ui


class ApiDemosPage:

    def accessibility_button(self):
        from Pages.accessibility.accessibility_page import AccessibilityPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Accessibility', AccessibilityPage)

    def animation_button(self):
        from Pages.animation.animation_page import AnimationPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Animation', AnimationPage)

    def app_button(self):
        from Pages.app.app_page import AppPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'App', AppPage)

    def content_button(self):
        from Pages.content.content_page import ContentPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Content', ContentPage)

    def graphics_button(self):
        from Pages.graphics.graphics_page import GraphicsPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Graphics', GraphicsPage)

    def media_button(self):
        from Pages.media.media_page import MediaPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Media', MediaPage)

    def nfc_button(self):
        from Pages.nfc.nfc_page import NfcPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'NFC', NfcPage)

    def os_button(self):
        from Pages.os.os_page import OsPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'OS', OsPage)

    def preference_button(self):
        from Pages.preference.preference_page import PreferencePage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Preference', PreferencePage)

    def text_button(self):
        from Pages.text.text_page import TextPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Text', TextPage)

    def views_button(self):
        from Pages.views.views_page import ViewsPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Views', ViewsPage)
