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
from logging import warning
from .page_decorator import PageDecorator
from .web_ui import WebUi
from .page_validator import page_validator
from .deprecated import logwarning


class WebPage:
    """
    an object class that use across the tests.
    contents_page are need to set if using page object strategy, it does not
    requied if only using this to access 'web.locate'.
    webdriver_wait is set '10' seconds by default
    logger is set 'True' by default

    Args:
        driver
    Kwargs (optional):
        contents_page
        webdriver_wait
        logger

    Usage:
        driver = webdriver.Chrome()
        web = WebPage(driver)
        or
        web = WebPage(driver) without contents_page to access "web.locate" only
    """
    def __init__(self, driver, webdriver_wait=10, logger=True):
        self._driver = driver
        self._webdriver_wait = webdriver_wait
        self._contents_page = None
        self._logger = logger

    @property
    def driver(self):
        """return the original selenium / appium driver."""
        return self._driver

    @property
    def page(self):
        """return a page decorator object of ContentsPage."""
        if not self._contents_page:
            warning('\n\tpage object hasn\'t been set yet.'
                    '\n\t"web = WebPage(driver, contents_page=ContentsPage)" '
                    'before "using web.page.foo.click()" etc.')
        return PageDecorator(self.driver, self._webdriver_wait, self._contents_page,
                             self._logger)

    @page.setter
    def page(self, new_page):
        self._contents_page = page_validator(new_page)

    def locate(self, by, value):
        """
        an alternative way for testing without page object and return WebUi
        class, but can't use page and back method and causing an error.
        good for quick prototype / write a tests.

        Args:
            by
            value

        Usage:
            web.locate(By.NAME, 'q').ec_presence_of_element_located()
            web.locate(By.NAME, 'q').get_element().text()
            web.locate(By.NAME, 'q').get_element().click()
        """
        return WebUi(self._driver, self._webdriver_wait, self._logger, by,
                     value, f'{by}: {value}', self.locate.__name__)

    def ready_state(self, timeout=30):
        """execute javascript for page to fully load"""
        for x in range(timeout):
            if self.driver.execute_script(
                    'return document.readyState') != 'complete':
                sleep(1)

    def webdriver_wait(self, wait):
        """override webdriver wait."""
        self._webdriver_wait = wait

    def sleep(self, time):
        """use time.sleep module to manually wait."""
        sleep(time)
