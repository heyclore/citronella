import pytest
from Pages.home.home_page import HomePage
from logging import getLogger


class TestUsageDemo:
    # not really a tests, just a weird way to try to make a documentation usage
    # with a limited english proficiency, limited experience, social issue.


    ### citronella.SelfBrowser ###

    def test_driver(self):
        # get the original selenium driver object
        # foo = self.browser.driver.find_element(By.ID, 'foo')

        self.browser.driver.get('https://pypi.org/')
        driver = self.browser.driver
        getLogger().warning(f'driver : {driver}')

    def test_page_object(self):
        # add page object for current url
        # this class can hold up to 3 history's and page object.

        self.browser.page_object(HomePage)
        getLogger().warning(f'page_object : {HomePage}')

    def test_page(self):
        # get a decorated page object

        page = self.browser.page
        getLogger().warning(f'page: {page}')
        self.browser.page.login_button.click()

    def test_back(self):
        # return to previous page
        # this class can hold up to 3 history's and page object.
        # when this command executed, the current page object get deleted
        # to previous url and page object

        self.browser.back()
        getLogger().warning(f'back: {self.browser.back}')

    def test_get_window_size(self):
        # get current browser height or width

        height = self.browser.get_window_size.height
        getLogger().warning(f'height: {height}')

        width = self.browser.get_window_size.width
        getLogger().warning(f'width: {width}')

    def test_ready_state(self):
        # execute javascript ready_state for wait to page fully to load
        # it's always executed by default after click / redirect to new url

        self.browser.ready_state

    def test_sleep(self):
        # forwarding time.sleep module, it may useful for debugging

        self.browser.sleep(1)
        getLogger().warning(f'sleep: {self.browser.sleep}')


    ### citronella.Ui ###

    def test_send_keys(self):
        # webdriver send_keys with optional clear input before insert the text

        self.browser.page.search_input.send_keys('citronella')
        self.browser.page.search_input.send_keys('citro', clear=True)
        getLogger().warning(f'send_keys: {self.browser.page.search_input.send_keys}')

    def test_click(self):
        # webdriver click

        self.browser.page.search_button.click()
        getLogger().warning(f'click: {self.browser.page.search_button.click}')

    def test_get_attribute(self):
        # webdriver get_attribute

        id = self.browser.page.order_by_option.get_attribute('id')
        class_name = self.browser.page.order_by_option.get_attribute('class')
        name = self.browser.page.order_by_option.get_attribute('name')
        getLogger().warning(f'id: {id}, class: {class_name}, name: {name}')

    def test_get_element(self):
        # webdriver get_element

        element = self.browser.page.order_by_option.get_element()
        getLogger().warning(f'element: {element}')

    def test_get_elements(self):
        # webdriver get_elements

        elements = self.browser.page.search_lists_result.get_elements()
        for x in elements:
            getLogger().warning(f'element: {x.text}')

    def test_text(self):
        # webdriver text
        self.browser.page.search_input.send_keys('citronella', clear=True)
        self.browser.page.search_button.click()
        result = self.browser.page.search_lists_result.get_element().text
        getLogger().warning(f'result: {result}')
