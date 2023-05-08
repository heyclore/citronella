import pytest
from selenium import webdriver
from citronella import WebPage


@pytest.fixture(scope='class', autouse=True)
def web(request):
    driver = webdriver.Chrome()
    yield WebPage(driver)
    driver.quit()
