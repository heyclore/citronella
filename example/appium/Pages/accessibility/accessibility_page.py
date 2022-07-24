from appium.webdriver.common.appiumby import AppiumBy
from citronella import Ui


class CustomViewPage:
    ACTIVITY = '.accessibility.CustomViewAccessibilityActivity'

class AccessibilityPage:

    def accessibility_node_provider_button(self):
        from .accessibility_node_provider.accessibility_node_provider_page import AccessibilityNodeProviderPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Accessibility Node Provider',
                AccessibilityNodeProviderPage)

    def accessibility_node_querying_button(self):
        from .accessibility_node_querying.accessibility_node_querying_page import AccessibilityNodeQueryingPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Accessibility Node Querying',
                AccessibilityNodeQueryingPage)

    def accessibility_service_button(self):
        from .accessibility_service.accessibility_service_page import AccessibilityServicePage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Accessibility Service',
                AccessibilityServicePage)

    def custom_view_button(self):
        from .custom_view.custom_view_page import CustomViewPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Custom View', CustomViewPage)
