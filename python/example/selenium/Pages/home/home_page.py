from selenium.webdriver.common.by import By
from citronella import Ui
from Pages.components import Header, Footer


class HomePage(Header, Footer):
    def browse_project_button(self):
        from Pages.search.search_page import SearchPage
        return Ui(By.XPATH, '//button[@type="submit"]/i', SearchPage)
