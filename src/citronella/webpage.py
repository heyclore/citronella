from types import SimpleNamespace
from time import sleep
from .page_decorator import Page_Decorator


class WebPage:
    """
    an object class that use across the tests.

    Args:
        webdriver

    Usage:
        driver = webdriver.Chrome()
        web = WebPage(driver)
    """
    def __init__(self, driver):
        self._page = []
        self._driver = driver
        self._ready_state = True
        self._app = 'appium' in str(driver.__class__)

    @property
    def driver(self):
        """return webdriver object."""
        return self._driver

    @property
    def page(self):
        """return latest page object model after execute ready_state func."""
        self.ready_state
        return Page_Decorator(self._page[-1], self.driver, self.page_object)

    def page_object(self, new_page):
        """
        initialize page object module object.

        Args:
            page_object_model

        Usage:
            self.browser.page_object(Homepage)
        """
        self._page.append(new_page)
        if len(self._page) > 3:
            self._page.pop(0)

    @property
    def get_window_size(self):
        """
        get current windows size.

        Usage:
            height = self.browser.get_window_size.height
            width = self.browser.get_window_size.width
        """
        return SimpleNamespace(**self.driver.get_window_size())

    @property
    def ready_state_toggle(self):
        """switch ready_state bool"""
        self._ready_state = not self._ready_state

    @property
    def ready_state(self):
        """execute javascript for page to fully load, disabled for appium"""
        if self._ready_state and not self._app:
            while self.driver.execute_script(
                    'return document.readyState') != 'complete': sleep(1)

    def sleep(self, time):
        """use time.sleep module to manually wait."""
        sleep(time)

    def back(self):
        """return to previous page."""
        self.driver.back()
        self._page.pop()
