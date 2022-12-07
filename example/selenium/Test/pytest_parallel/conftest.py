from selenium import webdriver
from citronella import WebPage
import pytest


@pytest.fixture(scope='function', autouse=True)
def web(request):
    driver = webdriver.Chrome()
    yield WebPage(driver)
    driver.quit()
