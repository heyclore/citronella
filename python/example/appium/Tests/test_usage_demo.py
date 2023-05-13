import pytest
from Pages.contents_page import ContentsPage


class TestUsageDemo:

    def test_driver(self, web):
        foo = 'citronella'
        web.page = ContentsPage
        web.page.home_page.gallery_button.click()
        web.page.gallery_page.text_input.send_keys(foo)
        web.page.gallery_page.add_button.click()
        bar = web.page.gallery_page.text_lists.get_elements()
        assert foo in [x.text for x in bar]
