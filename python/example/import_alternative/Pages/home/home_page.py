from selenium.webdriver.common.by import By
from citronella import ui
from Pages.components import Header, Footer
from Pages.module import Module


class HomePage(Header, Footer):
    def browse_project_button(self):
        return ui(By.XPATH, '//button[@type="submit"]/i', Module.search_page())
