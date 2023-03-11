from selenium.webdriver.common.by import By
from citronella import ui


class ProjectsPage(ContentsPage.header(), ContentsPage.sidebar_account()):
    def your_project_lists(self):
        return ui(By.CLASS_NAME, 'package-snippet__title')
