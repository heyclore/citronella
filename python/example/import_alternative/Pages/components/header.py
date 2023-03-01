from selenium.webdriver.common.by import By
from citronella import ui
from Pages.module import Module


class Header:
    def home_page_icon_menu(self):
        return ui(By.CLASS_NAME, 'site-header__logo', Module.home_page())

    def help_button(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][1]', Module.help_page())

    def sponsors_button(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][2]', Module.sponsors_page())

    def login_button(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][3]', Module.login_page())

    def register_button(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][4]', Module.register_page())

    def search_input(self):
        return ui(By.ID, 'search', Module.search_page())

    def search_button(self):
        return ui(By.XPATH, '//button[@type="submit"]/i', Module.search_page())
