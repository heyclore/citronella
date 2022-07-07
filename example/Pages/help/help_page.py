from selenium.webdriver.common.by import By
from citronella import Ui
from Pages.components import Header, Footer


class HelpPage(Header, Footer):
    def basics_link(self):
        return Ui(By.XPATH, '//a[@href="#basics"]')

    def my_account_link(self):
        return Ui(By.XPATH, '//a[@href="#my-account"]')
