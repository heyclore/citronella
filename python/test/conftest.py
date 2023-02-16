from selenium import webdriver
#from citronella import WebPage
from src.citronella import WebPage
import pytest

class Webdriver:
    def get(self, url):
        pass
    def driver(self):
        pass
    def quit(self):
        pass
    def find_element(self, x, y):
        return self
    def is_enabled(self):
        return True
    def is_displayed(self):
        return True
    def click(self):
        pass
    def execute_script(self,x):
        return 'complete'
    def back(self):
        pass

@pytest.fixture(scope='class', autouse=True)
def web(request):
    #driver = webdriver.Chrome()
    driver = Webdriver()
    yield WebPage(driver)
    driver.quit()
