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


from types import SimpleNamespace
from time import sleep
from .page_decorator import PageDecorator
from .page_tab import PageTab
from .web_ui import WebUi


class WebPage:
    """
    an object class that use across the tests.
    webdriver_wait is set '10' seconds by default
    logger is set 'True' by default

    Args:
        driver
    Kwargs (optional):
        webdriver_wait
        logger

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
        """return the original selenium / appium driver."""
        return self._driver

    @property
    def page(self):
        """return last page object model."""
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

    def locate(self, by, value):
        """
        an alternative way for testing without page object and return WebUi
        class, but can't use page and back method and causing an error.
        good for quick prototype / write a tests.

        Args:
            by
            value

        Usage:
            web.ui(By.NAME, 'q').ec_presence_of_element_located()
            web.ui(By.NAME, 'q').get_element().text()
            web.ui(By.NAME, 'q').get_element().click()
        """
        return WebUi(self._driver, self._webdriver_wait, self._pages,
                     self._logger, by, value, None, self.locate.__name__,
                     self.__class__.__name__)

    @property
    def back(self):
        """return to previous page and delete the last page object."""
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

    def ready_state(self, wait):
        """execute javascript for page to fully load, disabled for appium"""
        if not self._app:
            for x in range(wait):
                if self.driver.execute_script(
                        'return document.readyState') != 'complete':
                    sleep(1)

    def webdriver_wait(self, wait):
        """override webdriver wait."""
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
        warning("ready_state_toggle module is deprecated and will be removed in the next version.")
        warning("will remove this method for next version")
    #MARK TO REMOVE }
