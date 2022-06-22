from types import SimpleNamespace
from time import sleep
from .page_decorator import Page_Decorator


class WebBrowser:
    """
    a browser class that use across the tests.

    Args:
        webdriver

    Usage:
        driver = webdriver.Chrome()
        browser = WebBrowser(driver)
    """
    def __init__(self, driver):
        self._page = []
        self._driver = driver

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
            Homepage

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
    def ready_state(self):
        """execute javascript for page to fully load."""
        while self.driver.execute_script(
                'return document.readyState') != 'complete': sleep(1)

    def sleep(self, time):
        """use time.sleep module to manually wait."""
        sleep(time)

    def back(self, change_page=True):
        """
        return to previous page, if the current url doesn't have pom, use False
        as keyword arguments.

        Args:
            change_page=False

        Usage:
            self.browser.link_to_url_with_no_pom_object.click()
            self.browser.back(change_page=False)
        """
        self.driver.back()
        if not change_page:
            return

        self._page.pop()

    def quit(self):
        """quit selenium webdriver session."""
        self.driver.quit()
