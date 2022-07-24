import pytest
from Pages.account.login.login_page import LoginPage


class TestAuth:
    # not really a tests.
    # this may be use for expecting a tests to be fail.

    @pytest.mark.xfail(raises=AssertionError)
    def test_login_fail(self):
        self.web.driver.get('https://pypi.org/account/login/')
        self.web.page_object(LoginPage)

        self.web.page.username_input.send_keys('foo')
        self.web.page.password_input.send_keys('bar')
        self.web.page.login_button.click()
        assert 'projects' in self.web.driver.title
        # at this point current page object should change to a project pom

    def test_login_expect_fail(self):
        self.web.page_object(LoginPage)

        self.web.page.username_input.send_keys('foo', clear=True)
        self.web.page.password_input.send_keys('bar', clear=True)
        self.web.page.login_button.click(switch_page=False)
        # add 'switch_page=False' to prevent change page object model
        assert 'Log' in self.web.driver.title
