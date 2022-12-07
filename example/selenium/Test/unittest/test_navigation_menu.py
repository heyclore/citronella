import unittest, logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from citronella import WebPage, Ui, PlaceholderPage


class Header:
    def home_page_icon_menu(self):
        return Ui(By.CLASS_NAME, 'site-header__logo', HomePage)

    def help_button(self):
        return Ui(By.XPATH, '//li[@class="horizontal-menu__item"][1]', HelpPage)

    def sponsors_button(self):
        return Ui(By.XPATH, '//li[@class="horizontal-menu__item"][2]', SponsorPage)

    def login_button(self):
        return Ui(By.XPATH, '//li[@class="horizontal-menu__item"][3]', LoginPage)

    def register_button(self):
        return Ui(By.XPATH, '//li[@class="horizontal-menu__item"][4]', PlaceholderPage)

    def search_input(self):
        return Ui(By.ID, 'search')

    def search_button(self):
        return Ui(By.XPATH, '//button[@type="submit"]/i', SearchPage)


class HomePage(Header):
    def search_input(self):
        return Ui(By.ID, 'search')

    def search_button(self):
        return Ui(By.XPATH, '//button[@type="submit"]/i', SearchPage)


class SearchPage(Header):
    def search_lists_result(self):
        return Ui(By.XPATH, '//span[@class="package-snippet__name"]')


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
        self.web.ready_state_toggle
        self.web.driver.get('https://pypi.org/')
        self.web.page_object(HomePage)

        self.web.page.help_button.click()
        assert 'Help' in self.web.driver.title

        self.web.page.sponsors_button.click()
        assert 'Sponsors' in self.web.driver.title

        self.web.page.login_button.click()
        assert 'Log' in self.web.driver.title

        self.web.page.register_button.click()
        assert 'Create' in self.web.driver.title


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    unittest.main()
