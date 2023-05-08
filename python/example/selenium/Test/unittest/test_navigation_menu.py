import unittest, logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from citronella import WebPage, ui


class ContentsPage:
    def home_page(self):
        return HomePage

    def search_page(self):
        return SearchPage

    def help_page(self):
        return HelpPage

    def sponsors_page(self):
        return SponsorPage

    def login_page(self):
        return LoginPage


class Header:
    def home_page_icon_menu(self):
        return ui(By.CLASS_NAME, 'site-header__logo')

    def help_button(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][1]')

    def sponsors_button(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][2]')

    def login_button(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][3]')

    def register_button(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][4]')

    def search_input(self):
        return ui(By.ID, 'search')

    def search_button(self):
        return ui(By.XPATH, '//button[@type="submit"]/i')


class HomePage(Header):
    def search_input(self):
        return ui(By.ID, 'search')

    def search_button(self):
        return ui(By.XPATH, '//button[@type="submit"]/i')


class SearchPage(Header):
    def search_lists_result(self):
        return ui(By.XPATH, '//span[@class="package-snippet__name"]')

class HelpPage(Header): pass
class SponsorPage(Header): pass
class LoginPage(Header): pass


class NavigationMenu(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        self.web = WebPage(driver)

    def tearDown(self):
        self.web.driver.quit()
    
    def test_help_page(self):
        self.web.driver.get('https://pypi.org/')
        self.web.page = ContentsPage

        self.web.page.home_page.help_button.click()
        assert 'Help' in self.web.driver.title

        self.web.page.help_page.sponsors_button.click()
        assert 'Sponsors' in self.web.driver.title

        self.web.page.sponsors_page.login_button.click()
        assert 'Log' in self.web.driver.title

        self.web.page.login_page.register_button.click()
        assert 'Create' in self.web.driver.title


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    unittest.main()
