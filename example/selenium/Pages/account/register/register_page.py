from selenium.webdriver.common.by import By
from citronella import Ui
from Pages.components import Header, Footer


class RegisterPage(Header, Footer):
    ACTIVITY = 'https://pypi.org/account/register/'

    def full_name_input(self):
        return Ui(By.ID, 'full_name')

    def email_input(self):
        return Ui(By.ID, 'email')

    def username_input(self):
        return Ui(By.ID, 'username')

    def password_input(self):
        return Ui(By.ID, 'new_password')

    def password_confirm_input(self):
        return Ui(By.ID, 'password_confirm')
