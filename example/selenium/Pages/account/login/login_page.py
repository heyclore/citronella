from selenium.webdriver.common.by import By
from citronella import Ui
from Pages.components import Header, Footer


class LoginPage(Header, Footer):
    def username_input(self):
        return Ui(By.ID, 'username')

    def password_input(self):
        return Ui(By.ID, 'password')

    def login_button(self):
        from Pages.manage.projects.projects_page import ProjectsPage
        return Ui(By.XPATH, '//input[@type="submit"]', ProjectsPage)
