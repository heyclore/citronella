import pytest
from Pages.api_demos_page import ApiDemosPage
from Pages.animation.bouncing_balls.bouncing_balls_page import BouncingBallsPage


class TestUsageDemo:
    # not really a tests, just a weird way to try to make a documentation usage
    # with a limited english proficiency, limited experience.


    ### citronella.SelfBrowser ###

    def test_driver(self):
        # get the original selenium driver object.
        # foo = self.web.driver.find_element(By.ID, 'foo')

        driver = self.web.driver


    def test_page_object(self):
        # add page object for current url.
        # this class can hold up to 3 history's and page object.
        # args: POM class
        # optional kwargs: get_start=True.

        self.web.page_object(ApiDemosPage)

        # an alternative way if the page object provide an 'ACTIVITY' constant
        # variable with url value.
        # it's equal as self.web.driver.start_activity(pkg_name, activity)

        self.web.page_object(BouncingBallsPage, get_start=True)


    def test_page(self):
        # get a decorated page object.

        self.web.driver.start_activity(self.web._app, '.ApiDemos')
        self.web.page_object(ApiDemosPage)

        page = self.web.page
        self.web.page.accessibility_button.click()


    def test_back(self):
        # this class / object can hold up to 3 history's and page object.
        # when this command executed, the current page object get switch
        # to previous url and page object.

        self.web.back


    def test_webdriver_wait(self):
        # set a webdriver wait.

        self.web.webdriver_wait(60)


    def test_get_window_size(self):
        # get current browser height or width.

        height = self.web.get_window_size.height
        width = self.web.get_window_size.width


    def test_sleep(self):
        # forwarding time.sleep module, it may useful for debugging.
        # args: number / int

        self.web.sleep(1)

        self.web.page.os_button.click()
        self.web.page.morse_code_button.click()



    ### citronella.Ui ###

    def test_send_keys(self):
        # webdriver send_keys with optional clear input before insert the text.
        # arg: text
        # kwargs: clear=bool


        self.web.page.morse_input.send_keys('citronella')
        self.web.page.morse_input.send_keys('citro', clear=True)


    def test_click(self):
        # webdriver click with optional switch page object interruption.
        # see example at 'test_auth.py'.
        # kwargs: switch_page=bool

        self.web.page.vibrate_button.click()


    def test_is_located(self):
        # get webdriver element state without wait in boolean (True / False).

        element = self.web.page.vibrate_button.is_located()


    def test_get_attribute(self):
        # webdriver get_attribute.
        # args: attribute name

        text = self.web.page.morse_input.get_attribute('text')
        class_name = self.web.page.morse_input.get_attribute('class')


    def test_get_element(self):
        # webdriver get_element.

        element = self.web.page.vibrate_button.get_element()


    def test_get_elements(self):
        # webdriver get_elements.

        elements = self.web.page.vibrate_button.get_elements()


    def test_text(self):
        # webdriver text.

        result = self.web.page.morse_input.get_element().text
