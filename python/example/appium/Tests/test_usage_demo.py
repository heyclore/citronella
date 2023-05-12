import pytest
from Pages.contents_page import ContentsPage


class TestUsageDemo:

    def test_driver(self, web):
        web.page = ContentsPage
        web.page.home_page.gallery_button.click()
