import pytest
from Pages.account.login.login_page import LoginPage


class TestAuth:

    def test_login_expect_fail(self, web):
        web.page_object(LoginPage, get_start=True)

        web.page.username_input.send_keys('foo')
        web.page.password_input.send_keys('bar')
        web.page.login_button.click(switch_page=False)
        assert 'Log' in web.driver.title
    
    def test_login_success(self, web):
        web.page.username_input.send_keys('real_username', clear=True)
        web.page.password_input.send_keys('real_password', clear=True)
        web.page.login_button.click()
        assert 'projects' in web.driver.title
