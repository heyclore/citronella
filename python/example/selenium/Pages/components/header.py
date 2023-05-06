from selenium.webdriver.common.by import By
from citronella import ui


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
