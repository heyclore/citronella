# Webdriver Extension with Page Object Wrapper

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vitae mauris ac nulla cursus efficitur. Sed finibus risus eleifend nulla tincidunt tristique. Praesent nibh risus, vestibulum non tincidunt tempor, fermentum et turpis. 

## Example Test
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vitae mauris ac nulla cursus efficitur.

```python
import pytest
from Pages.HomePage import HomePage


class TestNavigationMenu:
    def test_help_page(self):
        self.browser.driver.get('https://pypi.org/')
        self.browser.page_object(HomePage)
        
        self.browser.page.help_button.click()
        assert 'Help" in self.browser.driver.title

    def test_sponsors_page(self):
        self.browser.page.sponsors_button.click()
        assert 'Sponsors" in self.browser.driver.title

    def test_login_page(self):
        self.browser.page.login_button.click()
        assert 'Log" in self.browser.driver.title
        
    def test_register_page(self):
        self.browser.page.register_button.click()
        assert 'Register" in self.browser.driver.title
```
___
## Documentation

There's only 2 class import in this module.

* first module for `conftest.py`

```python
import pytest
from selenium import webdriver
from citronella import WebdriverExtension


@pytest.fixture(autouse=True, scope='class')
def init_browser(request):
    driver = webdriver.Chrome()
    browser = WebdriverExtension(driver)
    request.cls.browser = browser
    yield
    browser.quit()
```

* second module for `Page Object Model`

```python
from selenium.webdriver.common.by import By
from citronella import We
from Pages.component.HeaderMenu import HeaderMenu


class HomePage(HeaderMenu):

    def some_button(self):
        return We(by.XPATH, '//a[@name="foo"]')

    def search_input(self):
        return We(by.ID, 'search')
        
    def search_button(self):
        from Pages.SearchPage import SearchPage 
        return We(by.NAME, 'search-button', SearchPage)
```

___
# Usage
        
### citronella.WebdriverExtension

###### Args:
- webdriver

###### command lists:
- page
- page_object
- get_window_size
- ready_state
- sleep
- back

### citronella.We

###### Args:
- selenium_by
- string_locator
- new_page_object(optional)

###### returned object command lists:
- get_attribute
- get_element
- get_elements
- click
- send_keys
- text
