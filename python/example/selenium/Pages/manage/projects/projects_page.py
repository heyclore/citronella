from selenium.webdriver.common.by import By
from Pages.components import Header, SidebarAccount


class ProjectsPage(Header, SidebarAccount):
    def your_project_lists(self):
        return ui(By.CLASS_NAME, 'package-snippet__title')
