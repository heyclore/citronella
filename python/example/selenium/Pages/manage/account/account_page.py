from selenium.webdriver.common.by import By
from citronella import ui
from Pages.components import Footer, SidebarAccount


class AccountPage(Footer, SidebarAccount):
    def full_name_input(self):
        return ui(By.ID, 'name')

    def public_email_option(self):
        return ui(By.ID, 'public_email')

    def update_account_button(self):
        return ui(By.XPATH, '//input[@value="Update account"]')
