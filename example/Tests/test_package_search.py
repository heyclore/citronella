import pytest
from Pages.home.home_page import HomePage


class TestPackageSearch:

    def test_help_page(self):
        self.browser.driver.get('https://pypi.org/')
        self.browser.page_object(HomePage)

        self.browser.page.search_input.send_keys('citronella')
        self.browser.page.search_button.click()

        assert 'citronella' in self.browser.page.search_lists_result.get_element().text

        # an alternative
        assert 'citronella' in [x.text for x in
                self.browser.page.search_lists_result.get_elements()]
