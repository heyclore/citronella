import pytest
from Pages.home.home_page import HomePage


class TestNavigationMenu:

    def test_help_page(self, web):
        web.driver.get('https://pypi.org/')
        web.page_object(HomePage)

        web.page.help_button.click()
        assert 'Help' in web.driver.title

    def test_sponsors_page(self, web):
        web.driver.get('https://pypi.org/')
        web.page_object(HomePage)

        web.page.sponsors_button.click()
        assert 'Sponsors' in web.driver.title

    def test_login_page(self, web):
        web.driver.get('https://pypi.org/')
        web.page_object(HomePage)

        web.page.login_button.click()
        assert 'Log' in web.driver.title

    def test_register_page(self, web):
        web.driver.get('https://pypi.org/')
        web.page_object(HomePage)

        web.page.register_button.click()
        assert 'Create' in web.driver.title
