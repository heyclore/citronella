from selenium.webdriver.common.by import By
from citronella import ui
from Pages.contents_page import ContentsPage


class HelpPage(ContentsPage.header(), ContentsPage.footer()):
    def basics_link(self):
        return ui(By.XPATH, '//a[@href="#basics"]')

    def my_account_link(self):
        return ui(By.XPATH, '//a[@href="#my-account"]')
