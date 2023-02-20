import pytest
from selenium.webdriver.common.by import By
from src.citronella import Ui, ui


class SearchPage:
    def home_button(self):
        return Ui(By.XPATH, '//button[@type="submit"]/i', HomePage)

class HomePage:
    ACTIVITY = 'https://pypi.org/'
    def search_button(self):
        return ui(By.XPATH, '//button[@type="submit"]/i', SearchPage)


class TestNavigationMenu:

    def test_help_page(self, web):
        web.page_object(HomePage, get_start=True)
        web.driver.get('https://pypi.org/')
        web.page.search_button.click()
        web.page.home_button.click()
        web.ready_state_toggle
        web.ready_state
        web.back

    def test_sponsors_page(self, web):
        #web.page.sponsors_button.click()
        #assert 'Sponsors' in web.driver.title
        pass

    def test_login_page(self, web):
        #web.page.login_button.click()
        #assert 'Log' in web.driver.title
        pass

    def test_register_page(self, web):
        #web.page.register_button.click()
        #assert 'Create' in web.driver.title
        pass
