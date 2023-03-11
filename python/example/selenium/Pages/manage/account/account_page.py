from selenium.webdriver.common.by import By
from citronella import ui
from Pages.contents_page import ContentsPage


class AccountPage(ContentsPage.header(), ContentsPage.sidebar_account()):
    def full_name_input(self):
        return ui(By.ID, 'name')

    def public_email_option(self):
        return ui(By.ID, 'public_email')

    def update_account_button(self):
        return ui(By.XPATH, '//input[@value="Update account"]')
