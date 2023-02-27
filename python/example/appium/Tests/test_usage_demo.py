import pytest
from Pages.api_demos_page import ApiDemosPage
from Pages.animation.bouncing_balls.bouncing_balls_page import BouncingBallsPage


class TestUsageDemo:
    # not really a tests, just a weird way to try to make a documentation usage
    # with a limited english proficiency, limited experience.


    ### citronella.SelfBrowser ###

    def test_driver(self, web):
        # get the original selenium driver object.
        # foo = web.driver.find_element(By.ID, 'foo')

        driver = web.driver


    def test_page_object(self, web):
        # add page object for current url.
        # this class can hold up to 3 history's and page object.
        # args: POM class
        # optional kwargs: get_start=True.

        web.page_object(ApiDemosPage)

        # an alternative way if the page object provide an 'ACTIVITY' constant
        # variable with url value.
        # it's equal as web.driver.start_activity(pkg_name, activity)

        web.page_object(BouncingBallsPage, get_start=True)


    def test_page(self, web):
        # get a decorated page object.

        web.driver.start_activity(web._app, '.ApiDemos')
        web.page_object(ApiDemosPage)

        page = web.page
        web.page.accessibility_button.click()


    def test_back(self, web):
        # this class / object can hold up to 3 history's and page object.
        # when this command executed, the current page object get switch
        # to previous url and page object.

        web.back


    def test_webdriver_wait(self, web):
        # set a webdriver wait.

        web.webdriver_wait(60)


    def test_get_window_size(self, web):
        # get current browser height or width.

        height = web.get_window_size.height
        width = web.get_window_size.width


    def test_sleep(self, web):
        # forwarding time.sleep module, it may useful for debugging.
        # args: number / int

        web.sleep(1)

        web.page.os_button.click()
        web.page.morse_code_button.click()



    ### citronella.Ui ###

    def test_send_keys(self, web):
        # webdriver send_keys with optional clear input before insert the text.
        # arg: text
        # kwargs: clear=bool


        web.page.morse_input.send_keys('citronella')
        web.page.morse_input.send_keys('citro', clear=True)


    def test_click(self, web):
        # webdriver click with optional switch page object interruption.
        # see example at 'test_auth.py'.
        # kwargs: switch_page=bool

        web.page.vibrate_button.click()


    def test_is_located(self, web):
        # get webdriver element state without wait in boolean (True / False).

        element = web.page.vibrate_button.is_located()


    def test_get_attribute(self, web):
        # webdriver get_attribute.
        # args: attribute name

        text = web.page.morse_input.get_attribute('text')
        class_name = web.page.morse_input.get_attribute('class')


    def test_get_element(self, web):
        # webdriver get_element.

        element = web.page.vibrate_button.get_element()


    def test_get_elements(self, web):
        # webdriver get_elements.

        elements = web.page.vibrate_button.get_elements()


    def test_text(self, web):
        # webdriver text.

        result = web.page.morse_input.get_element().text
