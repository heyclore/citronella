import pytest
from Pages.home.home_page import HomePage
from logging import getLogger


class TestUsageDemo:
    # not really a tests, just a weird way to try to make a documentation usage
    # with a limited english proficiency, limited experience.


    ### citronella.SelfBrowser ###

    def test_driver(self):
        # get the original selenium driver object
        # foo = self.web.driver.find_element(By.ID, 'foo')

        self.web.driver.get('https://pypi.org/')
        driver = self.web.driver
        getLogger().warning(f'driver : {driver}')

    def test_page_object(self):
        # add page object for current url
        # this class can hold up to 3 history's and page object.
        # args: POM class

        self.web.page_object(HomePage)
        getLogger().warning(f'page_object : {HomePage}')

    def test_page(self):
        # get a decorated page object

        page = self.web.page
        getLogger().warning(f'page: {page}')
        self.web.page.login_button.click()

    def test_back(self):
        # return to previous page
        # this class can hold up to 3 history's and page object.
        # when this command executed, the current page object get switch
        # to previous url and page object

        self.web.back()
        getLogger().warning(f'back: {self.web.back}')

    def test_get_window_size(self):
        # get current browser height or width

        height = self.web.get_window_size.height
        getLogger().warning(f'height: {height}')

        width = self.web.get_window_size.width
        getLogger().warning(f'width: {width}')

    def test_ready_state(self):
        # execute javascript ready_state for wait to page fully to load
        # it's always executed by default after click / redirect to new url

        self.web.ready_state

    def test_sleep(self):
        # forwarding time.sleep module, it may useful for debugging
        # args: number / int

        self.web.sleep(1)
        getLogger().warning(f'sleep: {self.web.sleep}')


    ### citronella.Ui ###

    def test_send_keys(self):
        # webdriver send_keys with optional clear input before insert the text
        # arg: text
        # kwargs: clear=bool

        self.web.page.search_input.send_keys('citronella')
        self.web.page.search_input.send_keys('citro', clear=True)
        getLogger().warning(f'send_keys: {self.web.page.search_input.send_keys}')

    def test_click(self):
        # webdriver click with optional switch page object interruption
        # see example at 'test_auth.py'
        # kwargs: switch_page=bool

        self.web.page.search_button.click()
        getLogger().warning(f'click: {self.web.page.search_button.click}')

    def test_get_attribute(self):
        # webdriver get_attribute
        # args: attribute name

        id = self.web.page.order_by_option.get_attribute('id')
        class_name = self.web.page.order_by_option.get_attribute('class')
        name = self.web.page.order_by_option.get_attribute('name')
        getLogger().warning(f'id: {id}, class: {class_name}, name: {name}')

    def test_get_element(self):
        # webdriver get_element

        element = self.web.page.order_by_option.get_element()
        getLogger().warning(f'element: {element}')

    def test_get_elements(self):
        # webdriver get_elements

        elements = self.web.page.search_lists_result.get_elements()
        for x in elements:
            getLogger().warning(f'element: {x.text}')

    def test_text(self):
        # webdriver text
        self.web.page.search_input.send_keys('citronella', clear=True)
        self.web.page.search_button.click()
        result = self.web.page.search_lists_result.get_element().text
        getLogger().warning(f'result: {result}')
