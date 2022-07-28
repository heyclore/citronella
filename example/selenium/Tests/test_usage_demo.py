import pytest
from Pages.home.home_page import HomePage
from Pages.account.register.register_page import RegisterPage


class TestUsageDemo:
    # not really a tests, just a weird way to try to make a documentation usage
    # with a limited english proficiency, limited experience.


    ### citronella.SelfBrowser ###

    def test_driver(self):
        # get the original selenium driver object
        # foo = self.web.driver.find_element(By.ID, 'foo')

        self.web.driver.get('https://pypi.org/')
        driver = self.web.driver


    def test_page_object(self):
        # add page object for current url
        # this class can hold up to 3 history's and page object.
        # args: POM class
        # optional kwargs: get_start=True.

        self.web.page_object(HomePage)

        # an alternative way if the page object provide an 'ACTIVITY' constant
        # variable with url value. can be use to bypass self.web.driver.get(url)

        self.web.page_object(RegisterPage, get_start=True)


    def test_page(self):
        # get a decorated page object.

        page = self.web.page
        self.web.page.login_button.click()


    def test_back(self):
        # this class / object can hold up to 3 history's and page object.
        # when this command executed, the current page object get switch
        # to previous url and page object.

        self.web.back


    def test_webdriver_wait(self):
        # set a webdriver wait.

        self.web.webdriver_wait(60)


    def test_ready_state(self):
        # execute javascript ready_state for wait to page fully to load.
        # it's always executed by default after click / redirect to new url.

        self.web.ready_state


    def test_ready_state_toggle(self):
        # disable or enable ready_state javascript.

        self.web.ready_state_toggle


    def test_get_window_size(self):
        # get current browser height or width.

        height = self.web.get_window_size.height
        width = self.web.get_window_size.width


    def test_sleep(self):
        # forwarding time.sleep module, it may useful for debugging.
        # args: number / int

        self.web.sleep(1)



    ### citronella.Ui ###

    def test_send_keys(self):
        # webdriver send_keys with optional clear input before insert the text
        # arg: text
        # kwargs: clear=bool

        self.web.page.search_input.send_keys('citronella')
        self.web.page.search_input.send_keys('citro', clear=True)


    def test_click(self):
        # webdriver click with optional switch page object interruption
        # see example at 'test_auth.py'
        # kwargs: switch_page=bool

        self.web.page.search_button.click()


    def test_is_located(self):
        # get webdriver element state without wait in boolean (True / False)

        element = self.web.page.order_by_option.is_located()

    def test_get_attribute(self):
        # webdriver get_attribute
        # args: attribute name

        id = self.web.page.order_by_option.get_attribute('id')
        class_name = self.web.page.order_by_option.get_attribute('class')
        name = self.web.page.order_by_option.get_attribute('name')


    def test_get_element(self):
        # webdriver get_element

        element = self.web.page.order_by_option.get_element()


    def test_get_elements(self):
        # webdriver get_elements

        elements = self.web.page.search_lists_result.get_elements()


    def test_text(self):
        # webdriver text

        self.web.page.search_input.send_keys('citronella', clear=True)
        self.web.page.search_button.click()
        self.web.ready_state
        result = self.web.page.search_lists_result.get_element().text
