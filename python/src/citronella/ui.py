from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .logger import logger


class Ui:
    """a wrapped object of a web element."""
    def __init__(self, by, attr, page=None):
        self._locator = (by, attr)
        self._page = page
        self._driver = None
        self._page_object = None
        self._function_name = None
        self._class_name = None
        self._wait = None

    def _webdriver_wait(self, ec):
        """return a web element or elements."""
        return WebDriverWait(self._driver, self._wait).until(ec)

    def get_attribute(self, attribute):
        """return atrribute of web element."""
        return self._webdriver_wait(EC.presence_of_element_located(
            self._locator)).get_attribute(attribute)

    @logger
    def is_located(self):
        """return bool if element is located without wait"""
        self._wait = 2
        return True if self._webdriver_wait(
                EC.presence_of_all_elements_located(self._locator)) else False

    @logger
    def get_element(self):
        """return web element, equal as find_element."""
        return self._webdriver_wait(EC.presence_of_element_located(
            self._locator))

    @logger
    def get_elements(self):
        """return list of web element, equal as find_elements."""
        return self._webdriver_wait(EC.presence_of_all_elements_located(
            self._locator))

    @logger
    def click(self, switch_page=True):
        """click to web element."""
        self._webdriver_wait(EC.element_to_be_clickable(self._locator)).click()
        if self._page and switch_page:
            self._page_object(self._page)

    @logger
    def send_keys(self, text, clear=False):
        """custom webdriver send_keys with optional clear field."""
        element = self._webdriver_wait(
                EC.element_to_be_clickable(self._locator))
        if clear:
            element.clear()
        element.send_keys(text)

    @logger
    def text(self):
        """return text of web element."""
        return self.get_element().text
