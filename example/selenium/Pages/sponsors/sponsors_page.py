from selenium.webdriver.common.by import By
from citronella import Ui
from Pages.components import Header, Footer, PlaceholderPage


class SponsorPage(Header, Footer):
    def become_a_sponsor_button(self):
        return(By.XPATH, '//div/a[@title="External link"]', PlaceholderPage)
