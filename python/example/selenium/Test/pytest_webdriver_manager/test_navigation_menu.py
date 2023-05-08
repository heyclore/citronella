import pytest
from Pages.contents_page import ContentsPage


class TestNavigationMenu:

    def test_help_page(self, web):
        web.driver.get('https://pypi.org/')
        web.page = ContentsPage

        web.page.home_page.help_button.click()
        assert 'Help' in web.driver.title

    def test_sponsors_page(self, web):
        web.page.help_page.sponsors_button.click()
        assert 'Sponsors' in web.driver.title

    def test_login_page(self, web):
        web.page.sponsors_page.login_button.click()
        assert 'Log' in web.driver.title

    def test_register_page(self, web):
        web.page.login_page.register_button.click()
        assert 'Create' in web.driver.title
