import pytest
from Pages.home.home_page import HomePage


class TestNavigationMenu:

    def test_help_page(self, web):
        web.driver.get('https://pypi.org/')
        web.page_object(HomePage)
        web.ready_state_toggle

        web.page.help_button.click()
        assert 'Help' in web.driver.title

    def test_sponsors_page(self, web):
        web.page.sponsors_button.click()
        assert 'Sponsors' in web.driver.title

    def test_login_page(self, web):
        web.page.login_button.click()
        assert 'Log' in web.driver.title

    def test_register_page(self, web):
        web.page.register_button.click()
        assert 'Create' in web.driver.title

    def test_foo_bar_baz(self, web):
        web.page.register_button.ec_element_to_be_clickable()
        web.page.register_button.ec_presence_of_element_located()
        web.page.register_button.ec_presence_of_all_elements_located()
        web.page.register_button.ec_visibility_of_element_located()
        web.page.register_button.ec_visibility_of_all_elements_located()
        web.page.register_button.ec_visibility_of_any_elements_located()
        #web.page.register_button.ec_element_located_to_be_selected()
        #web.page.register_button.ec_invisibility_of_element_located()
        assert 'Create' in web.driver.title
