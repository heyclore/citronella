#MIT License
#
#Copyright (c) 2023 Eko Purnomo
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import \
        presence_of_element_located, presence_of_all_elements_located, \
        visibility_of_element_located, visibility_of_all_elements_located, \
        visibility_of_any_elements_located, invisibility_of_element_located, \
        element_located_to_be_selected, element_to_be_clickable
from .logger import logger
from .deprecated import logwarning


class WebUi:
    """a wrapped object of a web element."""
    def __init__(self, driver, webdriver_wait, logger, by, value,
                 function_name, class_name):
        self._driver = driver
        self._wait = webdriver_wait
        self._logger = logger
        self._locator = (by, value)
        self._function_name = function_name
        self._class_name = class_name

    def _webdriver_wait(self, ec):
        """return a web element or elements."""
        WebDriverWait(self._driver, self._wait)
        return WebDriverWait(self._driver, self._wait).until(ec)

    @logger
    def ec_element_to_be_clickable(self):
        """wrapper of EC.element_to_be_clickable"""
        return self._webdriver_wait(
                element_to_be_clickable(self._locator))

    @logger
    def ec_presence_of_element_located(self):
        """wrapper of EC.presence_of_element_located"""
        return self._webdriver_wait(
                presence_of_element_located(self._locator))

    @logger
    def ec_presence_of_all_elements_located(self):
        """wrapper of EC.presence_of_all_elements_located"""
        return self._webdriver_wait(
                presence_of_all_elements_located(self._locator))

    @logger
    def ec_visibility_of_element_located(self):
        """wrapper of EC.visibility_of_element_located"""
        return self._webdriver_wait(
                visibility_of_element_located(self._locator))

    @logger
    def ec_visibility_of_all_elements_located(self):
        """wrapper of EC.visibility_of_all_elements_located"""
        return self._webdriver_wait(
                visibility_of_all_elements_located(self._locator))

    @logger
    def ec_visibility_of_any_elements_located(self):
        """wrapper of EC.visibility_of_any_elements_located"""
        return self._webdriver_wait(
                visibility_of_any_elements_located(self._locator))

    @logger
    def ec_invisibility_of_element_located(self):
        """wrapper of EC.invisibility_of_element_located"""
        return self._webdriver_wait(
                invisibility_of_element_located(self._locator))

    @logger
    def ec_element_located_to_be_selected(self):
        """wrapper of EC.element_located_to_be_selected"""
        return self._webdriver_wait(
                element_located_to_be_selected(self._locator))

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
    def click(self):
        """click to web element."""
        try:
            self._webdriver_wait(element_to_be_clickable(self._locator)).click()
        except Exception as e:
            sleep(2)
            self._webdriver_wait(element_to_be_clickable(self._locator)).click()

    @logger
    def send_keys(self, text, clear=False, return_key=False):
        """custom webdriver send_keys with optional clear field."""
        element = self._webdriver_wait(presence_of_element_located(self._locator))

        if clear:
            element.clear()

        element.send_keys(text)

        if return_key:
            element.send_keys(Keys.RETURN)
