from selenium.webdriver.common.by import By
from citronella import ui
from Pages.contents_page import ContentsPage


class Header:
    def home_page_icon_menu(self):
        return ui(By.CLASS_NAME, 'site-header__logo', ContentsPage.home_page())

    def help_button(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][1]', ContentsPage.help_page())

    def sponsors_button(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][2]', ContentsPage.sponsors_page())

    def login_button(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][3]', ContentsPage.login_page())

    def register_button(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][4]', ContentsPage.register_page())

    def search_input(self):
        return ui(By.ID, 'search', ContentsPage.search_page())

    def search_button(self):
        return ui(By.XPATH, '//button[@type="submit"]/i', ContentsPage.search_page())
