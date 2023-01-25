from types import SimpleNamespace
from time import sleep
from .page_decorator import PageDecorator


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
        self.driver = driver
        self._webdriver_wait = 8
        self._page = []
        self._ready_state = True
        self._app = driver.current_package if 'appium' in str(
                driver.__class__) else None

    @property
    def page(self):
        """return latest page object model after execute ready_state func."""
        self.ready_state
        return PageDecorator(self._page[-1], self.driver, self.page_object,
                self._webdriver_wait)

    def page_object(self, new_page, get_start=False):
        """
        initialize page object module object, get_start kwargs is optional and
        it set to FALSE by default, it can be use if the page object have
        an ACTIVITY constant variable.
        in selenium:
        it's equal as self.driver.get(url)
        in appium:
        it's equal as self.driver.start_activity(package_name, activity_name)

        Args:
            page_object_model

        Kwargs:
            get_start=True

        Usage:
            self.browser.page_object(Homepage)
            or
            self.browser.page_object(Homepage, get_start=True)
        """
        self._page.append(new_page)
        if len(self._page) > 3:
            self._page.pop(0)
        if get_start:
            if 'ACTIVITY' not in dir(new_page):
                raise ValueError(
                        f'ACTIVITY is not exist in {new_page.__qualname__}')
            if self._app:
                return self.driver.start_activity(self._app, new_page.ACTIVITY)
            self.driver.get(new_page.ACTIVITY)

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
    def ready_state(self):
        """execute javascript for page to fully load, disabled for appium"""
        if self._ready_state and not self._app:
            while self.driver.execute_script(
                    'return document.readyState') != 'complete': sleep(1)

    @property
    def ready_state_toggle(self):
        """switch ready_state bool"""
        self._ready_state = not self._ready_state

    def webdriver_wait(self, wait):
        """set webdriver wait."""
        self._webdriver_wait = wait

    def sleep(self, time):
        """use time.sleep module to manually wait."""
        sleep(time)

    @property
    def back(self):
        """return to previous page."""
        self.driver.back()
        self._page.pop()
