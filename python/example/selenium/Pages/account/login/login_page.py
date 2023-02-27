from selenium.webdriver.common.by import By
from citronella import ui
from Pages.components import Header, Footer


class LoginPage(Header, Footer):
    ACTIVITY = 'https://pypi.org/account/login/'

    def username_input(self):
        return ui(By.ID, 'username')

    def password_input(self):
        return ui(By.ID, 'password')

    def login_button(self):
        from Pages.manage.projects.projects_page import ProjectsPage
        return ui(By.XPATH, '//input[@type="submit"]', ProjectsPage)
