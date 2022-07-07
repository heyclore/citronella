from selenium.webdriver.common.by import By
from citronella import Ui
from Pages.components import Footer, SidebarAccount


class AccountPage(Footer, SidebarAccount):
    def full_name_input(self):
        return Ui(By.ID, 'name')

    def public_email_option(self):
        return Ui(By.ID, 'public_email')

    def update_account_button(self):
        return Ui(By.XPATH, '//input[@value="Update account"]')
