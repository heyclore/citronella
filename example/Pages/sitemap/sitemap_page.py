from selenium.webdriver.common.by import By
from citronella import Ui
from Pages.components import Header, Footer


class SiteMapPage(Header, Footer):
    def pypi_home_link(self):
        from Pages.home.home_page import HomePage
        return Ui(By.CLASS_NAME, 'site-header__logo', HomePage)

    def search_and_filter_projects_link(self):
        from Pages.search.search_page import SearchPage
        return Ui(By.XPATH, '//button[@type="submit"]/i', SearchPage)

    def help_link(self):
        from Pages.help.help_page import HelpPage
        return Ui(By.XPATH, '//li[@class="horizontal-menu__item"][1]', HelpPage)
