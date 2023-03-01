from selenium.webdriver.common.by import By
from citronella import ui


class SidebarAccount:
    def your_projects_button(self):
        return ui(By.XPATH, '//a[@href="/manage/projects/"]')

    def account_settings_button(self):
        return ui(By.XPATH, '//a[@href="/manage/account/"]')
