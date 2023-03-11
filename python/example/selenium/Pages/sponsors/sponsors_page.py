from selenium.webdriver.common.by import By
from citronella import ui, PlaceholderPage
from Pages.contents_page import ContentsPage


class SponsorPage(ContentsPage.header(), ContentsPage.footer()):
    def become_a_sponsor_button(self):
        return(By.XPATH, '//div/a[@title="External link"]', PlaceholderPage)
