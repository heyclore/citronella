import pytest
from selenium.webdriver.common.by import By


class TestWithoutPageObject:

    def test_navigation(self, web):
        web.driver.get('https://pypi.org/')

        web.locate(By.XPATH, '//li[@class="horizontal-menu__item"][1]').click()
        assert 'Help' in web.driver.title

        web.locate(By.XPATH, '//li[@class="horizontal-menu__item"][2]').click()
        assert 'Sponsors' in web.driver.title

        web.locate(By.XPATH, '//li[@class="horizontal-menu__item"][3]').click()
        assert 'Log' in web.driver.title

        web.locate(By.XPATH, '//li[@class="horizontal-menu__item"][4]').click()
        assert 'Create' in web.driver.title

    def test_search_package(self, web):
        web.locate(By.ID, 'search').get_element().send_keys('citronella')
        web.locate(By.XPATH, '//button[@type="submit"]/i').get_element().click()
        results = web.locate(By.XPATH, '//span[@class="package-snippet__name"]').get_elements()
        assert 'citronella' in [x.text for x in results]
