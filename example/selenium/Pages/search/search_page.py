from selenium.webdriver.common.by import By
from citronella import Ui
from Pages.components import Header, Footer


class SearchPage(Header, Footer):
    def search_lists_result(self):
        return Ui(By.XPATH, '//span[@class="package-snippet__name"]')

    def order_by_option(self):
        return Ui(By.ID, 'order')
