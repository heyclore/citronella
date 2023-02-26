import pytest
from Pages.home.home_page import HomePage
from selenium.webdriver.common.by import By


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

    def test_locate(self, web):
        web.locate(By.ID, 'search').send_keys('citrone')
        web.locate(By.XPATH, '//button[@type="submit"]/i').click()
        assert 'citronella' in [x.text for x in web.locate(By.XPATH,
        '//span[@class="package-snippet__name"]').get_elements()]

    def test_search_package(self, web):
        web.page.search_input.send_keys('citronella', return_key=True, clear=True)
        result = web.page.search_lists_result.get_elements()
        assert 'citronella' in [
                x.text for x in web.page.search_lists_result.get_elements()]
