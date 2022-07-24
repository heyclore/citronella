from appium.webdriver.common.appiumby import AppiumBy
from citronella import Ui, PlaceholderPage


class AnimationPage:

    def bouncing_balls_button(self):
        from .bouncing_balls.bouncing_balls_page import BouncingBallPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Bouncing Balls', BouncingBallPage)

    def cloning_button(self):
        from .cloning.cloning_page import CloningPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Cloning', CloningPage)

    def custom_evaluator_button(self):
        from .custom_evaluator.custom_evaluator_page import CustomEvaluatorPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Custom Evaluator', CustomEvaluatorPage)

    def default_layout_animations_button(self):
        from .default_layout.default_layout_page import DefaultLayoutPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Default Layout Animations', DefaultLayoutPage)

    def events_button(self):
        from .events.events_page import EventsPage
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Events', EventsPage)

    def hide_show_animations_button(self):
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Hide-Show Animations', PlaceholderPage)

    def layout_animations(self):
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Layout Animations', PlaceholderPage)

    def loading_button(self):
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Loading', PlaceholderPage)

    def multiple_properties_button(self):
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Multiple Properties', PlaceholderPage)

    def reversing_button(self):
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Reversing', PlaceholderPage)

    def seeking_button(self):
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'Seeking', PlaceholderPage)

    def view_flip_button(self):
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'View Flip', PlaceholderPage)
