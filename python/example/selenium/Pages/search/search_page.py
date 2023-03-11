from selenium.webdriver.common.by import By
from citronella import ui
from Pages.contents_page import ContentsPage


class SearchPage(ContentsPage.header(), ContentsPage.footer()):
    def search_lists_result(self):
        return ui(By.XPATH, '//span[@class="package-snippet__name"]')

    def order_by_option(self):
        return ui(By.ID, 'order')
