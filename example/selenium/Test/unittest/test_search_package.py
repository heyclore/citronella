import unittest, logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from citronella import WebPage, Ui, PlaceholderPage


class HomePage:
    def search_input(self):
        return Ui(By.ID, 'search')

    def search_button(self):
        return Ui(By.XPATH, '//button[@type="submit"]/i', SearchPage)


class SearchPage:
    def search_lists_result(self):
        return Ui(By.XPATH, '//span[@class="package-snippet__name"]')


class SearchPackage(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        self.web = WebPage(driver)

    def tearDown(self):
        self.web.driver.quit()
    
    def test_help_page(self):
        self.web.driver.get('https://pypi.org/')
        self.web.page_object(HomePage)

        self.web.page.search_input.send_keys('citronella')
        self.web.page.search_button.click()
        result = self.web.page.search_lists_result.get_elements()
        assert 'citronella' in [x.text for x in result]


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    unittest.main()
