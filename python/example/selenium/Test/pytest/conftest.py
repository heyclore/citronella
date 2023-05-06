import pytest
from selenium import webdriver
from citronella import WebPage
from Pages.contents_page import ContentsPage


@pytest.fixture(scope='class', autouse=True)
def web(request):
    driver = webdriver.Chrome()
    yield WebPage(driver, contents_page=ContentsPage)
    driver.quit()
