# Citronella

[![PyPI version](https://badge.fury.io/py/citronella.svg)](https://badge.fury.io/py/citronella)
[![Downloads](https://pepy.tech/badge/citronella)](https://pepy.tech/project/citronella)

Citronella is a selenium webdriver extension with page object wrapper for create a tests a bit simple.

## Example Test
[a full documentation / demo examples here.](https://github.com/heyclore/citronella/tree/main/example)

```python
import pytest
from Pages.home.home_page import HomePage


class TestNavigationMenu:

    def test_help_page(self):
        self.web.driver.get('https://pypi.org/')
        self.web.page_object(HomePage)

        self.web.page.help_button.click()
        assert 'Help' in self.web.driver.title

    def test_sponsors_page(self):
        self.web.page.sponsors_button.click()
        assert 'Sponsors' in self.web.driver.title

    def test_login_page(self):
        self.web.page.login_button.click()
        assert 'Log' in self.web.driver.title

    def test_register_page(self):
        self.web.page.register_button.click()
        assert 'Create' in self.web.driver.title
```

___
## Install Package

```bash
pip install citronella
```

___
## Documentation

There's only 2 modules import in this package.

* first module for `conftest.py`

```python
import pytest
from selenium import webdriver
from citronella import WebPage


@pytest.fixture(autouse=True, scope='class')
def browser(request):
    driver = webdriver.Chrome()
    web = WebPage(driver)
    request.cls.web = web
    yield
    driver.quit()
```

* second and third module for `Page Object Model`

```python
from selenium.webdriver.common.by import By
from citronella import Ui, PlaceholderPage
from Pages.component.HeaderMenu import HeaderMenu


class HomePage(HeaderMenu):

    def some_button(self):
        return Ui(By.XPATH, '//a[@name="foo"]')

    def search_input(self):
        return Ui(By.ID, 'search')

    def search_button(self):
        from Pages.SearchPage import SearchPage
        return Ui(By.NAME, 'search-button', SearchPage)

    def link_to_somewhere_currently_dont_have_page_object(self):
        return Ui(By.NAME, 'search-button', PlaceholderPage)
```

___
## Usage

### citronella.WebPage

###### Args:
- webdriver

###### Method Lists:
- [driver]
- [page_object]
- [page]
- [back]
- [webdriver_wait]
- [ready_state]
- [ready_state_toggle]
- [get_window_size]
- [sleep]

### citronella.Ui

###### Args:
- selenium_by
- string_locator
- new_page_object

###### Method Lists:
- [send_keys]
- [click]
- [is_located]
- [get_attribute]
- [get_element]
- [get_elements]
- [text]
