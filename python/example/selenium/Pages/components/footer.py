from selenium.webdriver.common.by import By
from citronella import ui


class Footer:
    def site_map_button(self):
        return ui(By.XPATH, '//a[@href="/sitemap/"]')
