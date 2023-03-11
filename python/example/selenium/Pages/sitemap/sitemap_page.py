from selenium.webdriver.common.by import By
from citronella import ui
from Pages.contents_page import ContentsPage


class SiteMapPage(ContentsPage.header(), ContentsPage.footer()):
    def pypi_home_link(self):
        return ui(By.CLASS_NAME, 'site-header__logo', ContentsPage.home_page())

    def search_and_filter_projects_link(self):
        return ui(By.XPATH, '//button[@type="submit"]/i', ContentsPage.search_page())

    def help_link(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][1]', ContentsPage.help_page())
