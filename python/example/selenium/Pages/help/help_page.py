from selenium.webdriver.common.by import By
from citronella import ui
from Pages.components import Header, Footer


class HelpPage(Header, Footer):
    def basics_link(self):
        return ui(By.XPATH, '//a[@href="#basics"]')

    def my_account_link(self):
        return ui(By.XPATH, '//a[@href="#my-account"]')
