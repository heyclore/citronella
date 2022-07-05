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
from citronella import SelfBrowser


@pytest.fixture(autouse=True, scope='class')
def init_browser(request):
    driver = webdriver.Chrome()
    browser = SelfBrowser(driver)
    request.cls.browser = browser
    yield
    driver.quit()
```

* second module for `Page Object Model`

```python
from selenium.webdriver.common.by import By
from citronella import Ui
from Pages.component.HeaderMenu import HeaderMenu


class HomePage(HeaderMenu):

    def some_button(self):
        return Ui(By.XPATH, '//a[@name="foo"]')

    def search_input(self):
        return Ui(By.ID, 'search')

    def search_button(self):
        from Pages.SearchPage import SearchPage
        return Ui(By.NAME, 'search-button', SearchPage)
```

___
# Usage

### citronella.SelfBrowser

###### Args:
- webdriver

###### function lists:
- driver
- page
- page_object
- get_window_size
- ready_state
- sleep
- back

### citronella.Ui

###### Args:
- selenium_by
- string_locator
- new_page_object(optional)

###### function lists:
- get_attribute
- get_element
- get_elements
- click
- send_keys
- text
