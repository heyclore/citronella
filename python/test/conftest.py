from selenium import webdriver
from citronella import WebPage
import pytest


@pytest.fixture(scope='class', autouse=True)
def web(request):
    driver = webdriver.Chrome()
    yield WebPage(driver, logger=False)
    driver.quit()
