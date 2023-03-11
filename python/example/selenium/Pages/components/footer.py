from selenium.webdriver.common.by import By
from citronella import ui
from Pages.contents_page import ContentsPage


class Footer:
    def site_map_button(self):
        return ui(By.XPATH, '//a[@href="/sitemap/"]', ContentsPage.sitemap_page())
