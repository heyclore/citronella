from types import SimpleNamespace
from time import sleep
from .page_decorator import PageDecorator
from .page_tab import PageTab


class WebPage:
    """
    an object class that use across the tests.

    Args:
        webdriver

    Usage:
        driver = webdriver.Chrome()
        web = WebPage(driver)
    """
    def __init__(self, driver, webdriver_wait=10, logger=True):
        self._driver = driver
        self._webdriver_wait = webdriver_wait
        self._pages = PageTab()
        self._logger = logger
        self._app = driver.current_package if 'appium' in str(
                driver.__class__) else None

    @property
    def driver(self):
        return self._driver

    @property
    def page(self):
        """return latest page object model after execute ready_state func."""
        return PageDecorator(self.driver, self._webdriver_wait, self._pages,
                             self._logger)

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
        self._pages.append(new_page)
        if get_start:
            if 'ACTIVITY' not in dir(new_page):
                raise ValueError(
                        f'ACTIVITY is not exist in {new_page.__qualname__}')
            if self._app:
                return self.driver.start_activity(self._app, new_page.ACTIVITY)
            self.driver.get(new_page.ACTIVITY)

    @property
    def back(self):
        """return to previous page."""
        self.driver.back()
        self._pages.pop()

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
        if not self._app:
            for x in range(30):
                if self.driver.execute_script(
                        'return document.readyState') != 'complete':
                    sleep(1)

    def webdriver_wait(self, wait):
        """set webdriver wait."""
        self._webdriver_wait = wait

    def sleep(self, time):
        """use time.sleep module to manually wait."""
        sleep(time)

    #MARK TO REMOVE {
    @property
    def ready_state_toggle(self):
        """switch ready_state bool"""
        #self._ready_state = not self._ready_state
        from logging import warning
        warning("ready_state_toggle are decrepated !!!")
        warning("will remove this method for next version")
    #MARK TO REMOVE }
