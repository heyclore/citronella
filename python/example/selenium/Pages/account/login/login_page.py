from selenium.webdriver.common.by import By
from citronella import ui
from Pages.contents_page import ContentsPage


class LoginPage(ContentsPage().header(), ContentsPage().footer()):

    def username_input(self):
        return ui(By.ID, 'username')

    def password_input(self):
        return ui(By.ID, 'password')

    def login_button(self):
        return ui(By.XPATH, '//input[@type="submit"]')
