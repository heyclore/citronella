from selenium.webdriver.common.by import By
from citronella import ui
from Pages.contents_page import ContentsPage


class HomePage(ContentsPage.header(), ContentsPage.footer()):
    def browse_project_button(self):
        return ui(By.XPATH, '//button[@type="submit"]/i', ContentsPage.search_page())
