from selenium.webdriver.common.by import By
from citronella import Ui
from Pages.components import Footer, SidebarAccount


class ProjectsPage(Footer, SidebarAccount):
    def your_project_lists(self):
        return Ui(By.CLASS_NAME, 'package-snippet__title')
