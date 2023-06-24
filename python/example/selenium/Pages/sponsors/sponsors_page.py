from selenium.webdriver.common.by import By
from citronella import ui
from Pages.components import Header, Footer


class SponsorPage(Header, Footer):
    def become_a_sponsor_button(self):
        return(By.XPATH, '//div/a[@title="External link"]')
