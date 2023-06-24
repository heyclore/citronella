from selenium.webdriver.common.by import By
from citronella import ui
from Pages.components import Header, Footer


class SiteMapPage(Header, Footer):
    def pypi_home_link(self):
        return ui(By.CLASS_NAME, 'site-header__logo')

    def search_and_filter_projects_link(self):
        return ui(By.XPATH, '//button[@type="submit"]/i')

    def help_link(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][1]')
