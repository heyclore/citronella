from selenium.webdriver.common.by import By
from citronella import Ui


class Footer:
    def site_map_button(self):
        from Pages.sitemap.sitemap_page import SiteMapPage
        return Ui(By.XPATH, '//a[@href="/sitemap/"]', SiteMapPage)
