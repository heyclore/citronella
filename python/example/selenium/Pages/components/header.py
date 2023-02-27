from selenium.webdriver.common.by import By
from citronella import ui


class Header:
    def home_page_icon_menu(self):
        from Pages.home.home_page import HomePage
        return ui(By.CLASS_NAME, 'site-header__logo', HomePage)

    def help_button(self):
        from Pages.help.help_page import HelpPage
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][1]', HelpPage)

    def sponsors_button(self):
        from Pages.sponsors.sponsors_page import SponsorPage
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][2]', SponsorPage)

    def login_button(self):
        from Pages.account.login.login_page import LoginPage
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][3]', LoginPage)

    def register_button(self):
        from Pages.account.register.register_page import RegisterPage
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][4]', RegisterPage)

    def search_input(self):
        return ui(By.ID, 'search')

    def search_button(self):
        from Pages.search.search_page import SearchPage
        return ui(By.XPATH, '//button[@type="submit"]/i', SearchPage)
