from selenium.webdriver.common.by import By
from citronella import ui
from Pages.components import Header, Footer


class LoginPage(Header, Footer):

    def username_input(self):
        return ui(By.ID, 'username')

    def password_input(self):
        return ui(By.ID, 'password')

    def login_button(self):
        return ui(By.XPATH, '//input[@type="submit"]')
