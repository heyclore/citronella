import pytest, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from citronella import WebPage


username = os.environ.get("BROWSERSTACK_USERNAME")
accessKey = os.environ.get("BROWSERSTACK_ACCESS_KEY")
bstack_options = {
        'os' : 'Windows',
        'osVersion' : '10',
        'browserVersion': 'latest'
        }
options = Options()
options.set_capability('bstack:options', bstack_options)
options.set_capability('browserName', 'Chrome')

@pytest.fixture(scope='class', autouse=True)
def web(request):
    driver = webdriver.Remote(
            command_executor='https://'+username+':'+accessKey+'@hub.browserstack.com/wd/hub',
            options=options
            )
    yield WebPage(driver)
    driver.quit()
