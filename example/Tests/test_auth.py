import pytest
from Pages.account.login.login_page import LoginPage


class TestAuth:

    def test_login_fail(self):
        self.web.driver.get('https://pypi.org/account/login/')
        self.web.page_object(LoginPage)

        self.web.page.username_input.send_keys('foo')
        self.web.page.password_input.send_keys('bar')
        self.web.page.login_button.click(switch_page=False)
        # add 'switch_page=False' to prevent change page object model

        self.web.page.username_input.send_keys('foo', clear=True)
        self.web.page.password_input.send_keys('bar', clear=True)
        self.web.sleep(3)
