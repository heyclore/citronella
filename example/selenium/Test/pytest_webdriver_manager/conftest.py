from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from citronella import WebPage
import pytest


@pytest.fixture(scope='class', autouse=True)
def web(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield WebPage(driver)
    driver.quit()
