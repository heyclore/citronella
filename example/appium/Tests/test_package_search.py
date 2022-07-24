import pytest
from Pages.home.home_page import HomePage


class TestPackageSearch:

    def test_help_page(self):
        self.web.driver.get('https://pypi.org/')
        self.web.page_object(HomePage)

        self.web.page.search_input.send_keys('citronella')
        self.web.page.search_button.click()

        assert 'citronella' in self.web.page.search_lists_result.get_element().text

        # an alternative
        assert 'citronella' in [x.text for x in
                self.web.page.search_lists_result.get_elements()]
