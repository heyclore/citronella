import pytest
from Pages.home.home_page import HomePage


@pytest.mark.incremental
class TestNavigationMenu:

    def test_help_page(self):
        self.browser.driver.get('https://pypi.org/')
        self.browser.page_object(HomePage)

        self.browser.page.help_button.click()
        assert 'Help' in self.browser.driver.title

    def test_sponsors_page(self):
        self.browser.page.sponsors_button.click()
        assert 'Sponsors' in self.browser.driver.title

    def test_login_page(self):
        self.browser.page.login_button.click()
        assert 'Log' in self.browser.driver.title

    def test_register_page(self):
        self.browser.page.register_button.click()
        assert 'Create' in self.browser.driver.title
