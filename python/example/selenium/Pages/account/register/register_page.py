from selenium.webdriver.common.by import By
from citronella import ui
from Pages.contents_page import ContentsPage


class RegisterPage(ContentsPage.header(), ContentsPage.footer()):
    ACTIVITY = 'https://pypi.org/account/register/'

    def full_name_input(self):
        return ui(By.ID, 'full_name')

    def email_input(self):
        return ui(By.ID, 'email')

    def username_input(self):
        return ui(By.ID, 'username')

    def password_input(self):
        return ui(By.ID, 'new_password')

    def password_confirm_input(self):
        return ui(By.ID, 'password_confirm')
