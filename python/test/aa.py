import sys
import pytest
from selenium.webdriver.common.by import By
from citronella import ui, WebPage

class Header:
    def home_page_icon_menu(self):
        return ui(By.CLASS_NAME, 'site-header__logo')
    def sponsors_button(self):
        return ui(By.XPATH, '//li[@class="horizontal-menu__item"][2]')
class ContentsPage:
    def header(self):
        return Header
    def home_page(self):
        return HomePage
    def sponsors_page(self):
        return SponsorPage
class HomePage(ContentsPage().header()):
    def browse_project_button(self):
        return ui(By.XPATH, '//button[@type="submit"]/i')
    def browse_project_button2(self):
        return ui(By.XPATH, '//button[@type="submit"]/i',2)
class SponsorPage(ContentsPage().header()):
    def become_a_sponsor_button(self):
        return ui(By.XPATH, '//div/a[@title="External link"]')

class Foo:
    def find_element(self):
        return self
    def back(self):
        return self
    def get_window_size(self):
        return {'width':8, 'height': 8}

web = WebPage(Foo(), contents_page=ContentsPage)
web.page.home_page.browse_project_button.click
web.get_window_size
web.back
web.page.sponsors_page.become_a_sponsor_button.click(switch_page=False)
web.page.home_page.browse_project_button2.send_keys(1,switch_page=False)
web.page_object(ContentsPage)
