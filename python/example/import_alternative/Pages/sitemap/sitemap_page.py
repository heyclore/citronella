from selenium.webdriver.common.by import By
from citronella import ui
from Pages.components import Header, Footer
from Pages.module import Module


class SiteMapPage(Header, Footer):
    def pypi_home_link(self):
        return ui(By.CLASS_NAME, 'site-header__logo', Module.home_page())

    def search_and_filter_projects_link(self):
        return ui(By.XPATH, '//button[@type="submit"]/i', Module.search_page())

    def help_link(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][1]', Module.help_page())
