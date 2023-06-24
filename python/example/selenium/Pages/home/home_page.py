from selenium.webdriver.common.by import By
from citronella import ui
from Pages.components import Header, Footer


class HomePage(Header, Footer):
    def browse_project_button(self):
        return ui(By.XPATH, '//button[@type="submit"]/i')
