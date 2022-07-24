import pytest
from Pages.home.home_page import HomePage


@pytest.mark.incremental
class TestNavigationMenu:

    def test_help_page(self):
        self.web.driver.get('https://pypi.org/')
        self.web.page_object(HomePage)

        self.web.page.help_button.click()
        assert 'Help' in self.web.driver.title

    def test_sponsors_page(self):
        self.web.page.sponsors_button.click()
        assert 'Sponsors' in self.web.driver.title

    def test_login_page(self):
        self.web.page.login_button.click()
        assert 'Log' in self.web.driver.title

    def test_register_page(self):
        self.web.page.register_button.click()
        assert 'Create' in self.web.driver.title
