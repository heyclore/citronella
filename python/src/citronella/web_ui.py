from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import \
        presence_of_element_located, presence_of_all_elements_located, \
        visibility_of_element_located, visibility_of_all_elements_located, \
        visibility_of_any_elements_located, invisibility_of_element_located, \
        element_located_to_be_selected, element_to_be_clickable
from .logger import logger


class WebUi:
    """a wrapped object of a web element."""
    def __init__(self, driver, webdriver_wait, pages, logger, by, value,
                 new_page, function_name, class_name):
        self._driver = driver
        self._wait = webdriver_wait
        self._pages = pages
        self._logger = logger
        self._locator = (by, value)
        self._new_page = new_page
        self._function_name = function_name
        self._class_name = class_name

    def _webdriver_wait(self, ec):
        """return a web element or elements."""
        return WebDriverWait(self._driver, self._wait).until(ec)

    @logger
    def get_element(self):
        """return web element, equal as find_element."""
        return self._webdriver_wait(presence_of_element_located(
            self._locator))

    @logger
    def get_elements(self):
        """return list of web element, equal as find_elements."""
        return self._webdriver_wait(presence_of_all_elements_located(
            self._locator))

    @logger
    def click(self, switch_page=True):
        """click to web element."""
        self._webdriver_wait(element_to_be_clickable(self._locator)).click()
        if self._new_page and switch_page:
            self._pages.append(self._new_page)

    @logger
    def send_keys(self, text, clear=False):
        """custom webdriver send_keys with optional clear field."""
        element = self._webdriver_wait(element_to_be_clickable(self._locator))
        if clear:
            element.clear()
        element.send_keys(text)

    @logger
    def ec_presence_of_element_located(self):
        """redirect of EC.presence_of_element_located"""
        return self._webdriver_wait(
                presence_of_element_located(self._locator))

    @logger
    def ec_presence_of_all_elements_located(self):
        """redirect of EC.presence_of_all_elements_located"""
        return self._webdriver_wait(
                presence_of_all_elements_located(self._locator))

    @logger
    def ec_visibility_of_element_located(self):
        """redirect of EC.visibility_of_element_located"""
        return self._webdriver_wait(
                visibility_of_element_located(self._locator))

    @logger
    def ec_visibility_of_all_elements_located(self):
        """redirect of EC.visibility_of_all_elements_located"""
        return self._webdriver_wait(
                visibility_of_all_elements_located(self._locator))

    @logger
    def ec_visibility_of_any_elements_located(self):
        """redirect of EC.visibility_of_any_elements_located"""
        return self._webdriver_wait(
                visibility_of_any_elements_located(self._locator))

    @logger
    def ec_invisibility_of_element_located(self):
        """redirect of EC.invisibility_of_element_located"""
        return self._webdriver_wait(
                invisibility_of_element_located(self._locator))

    @logger
    def ec_element_located_to_be_selected(self):
        """redirect of EC.element_located_to_be_selected"""
        return self._webdriver_wait(
                element_located_to_be_selected(self._locator))


#MARK TO REMOVE {
    def get_attribute(self, attribute):
        from logging import warning
        warning("get_attribute are decrepated !!!")
        warning('use "web.page.foobar.get_element.get_attribute(attribute)" instead')
        return self._webdriver_wait(presence_of_element_located(
            self._locator)).get_attribute(attribute)

    @logger
    def is_located(self):
        from logging import warning
        warning("is_located are decrepated !!!")
        warning('use "web.page.foobar.ec_presence_of_element_located" instead')
        return True if self._webdriver_wait(
                presence_of_all_elements_located(self._locator)) else False

    @logger
    def text(self):
        from logging import warning
        warning("text are decrepated !!!")
        warning('use "web.page.foobar.get_element.text" instead')
        return self.get_element().text
#MARK TO REMOVE }
