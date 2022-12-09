# Citronella

[![PyPI version](https://badge.fury.io/py/citronella.svg)](https://badge.fury.io/py/citronella)
[![Downloads](https://pepy.tech/badge/citronella)](https://pepy.tech/project/citronella)

Citronella is a selenium and/or appium webdriver extension with page object wrapper for create a tests a bit simple.

![alt terminal](https://github.com/heyclore/citronella/blob/main/screenshot/terminal.png?raw=true)
![alt pytest-html](https://github.com/heyclore/citronella/blob/main/screenshot/pytest_html.png?raw=true)
![alt github-action](https://github.com/heyclore/citronella/blob/main/screenshot/github_action.png?raw=true)

## Example Test

### Selenium

```python
import pytest
from Pages.home.home_page import HomePage


class TestNavigationMenu:

    def test_help_page(self, web):
        web.driver.get('https://pypi.org/')
        web.page_object(HomePage)

        web.page.help_button.click()
        assert 'Help' in web.driver.title

    def test_sponsors_page(self, web):
        web.page.sponsors_button.click()
        assert 'Sponsors' in web.driver.title

    def test_login_page(self, web):
        web.page.login_button.click()
        assert 'Log' in web.driver.title

    def test_register_page(self, web):
        web.page.register_button.click()
        assert 'Create' in web.driver.title
```

### Appium

```python
import pytest
from Pages.api_demos_page import ApiDemosPage


class TestNavigationMenu:

    def test_accessibility_page(self, web):
        web.page_object(ApiDemosPage)

        web.page.accessibility_button.click()
        assert web.page.accessibility_node_provider_button.get_element().is_visible()

    def test_animation_page(self, web):
        web.back
        web.page.animation_button.click()
        assert web.page.cloning_button.get_element().is_visible()

    def test_app_page(self, web):
        web.back
        web.page.app_button.click()
        assert web.page.activity_button.get_element().is_visible()

    def test_os_page(self, web):
        web.back
        web.page.os_button.click()
        assert web.page.morse_code_button.get_element().is_visible()
```
___
## Install Package

```bash
pip install citronella
```

___
## Documentation

There's only 3 modules import in this package.

* first module for `conftest.py`

### Selenium

```python
import pytest
from selenium import webdriver
from citronella import WebPage


@pytest.fixture(autouse=True, scope='class')
def web(request):
    driver = webdriver.Chrome()
    yield WebPage(driver)
    driver.quit()
```

### Appium

```python
import pytest
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from citronella import WebPage


@pytest.fixture(autouse='true', scope='class')
def web(request):
    options = UiAutomator2Options()
    options.platformName = 'Android'
    options.app = os.getcwd() + '/APK/ApiDemos-debug.apk.zip'
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
    yield WebPage(driver)
    driver.quit()
```

* second and third module for `Page Object Model`

### Selenium

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

### Appium

```python
from appium.webdriver.common.appiumby import AppiumBy
from citronella import Ui, PlaceholderPage
from Pages.component.HeaderMenu import HeaderMenu


class HomePage(HeaderMenu):

    def some_button(self):
        return Ui(AppiumBy.XPATH, '//a[@name="foo"]')

    def search_input(self):
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'search')

    def search_button(self):
        from Pages.SearchPage import SearchPage
        return Ui(AppiumBy.ID, 'search-button', SearchPage)

    def link_to_somewhere_currently_dont_have_page_object(self):
        return Ui(AppiumBy.ACCESSIBILITY_ID, 'search-button', PlaceholderPage)
```

___
## Usage

### citronella.WebPage

###### Args:
- webdriver

###### Method Lists:
| Method Name        | Args*       | Kwargs**         | Note |
| ------------------ |:-----------:|:----------------:|:----:|
| driver             | None        | None             |      |
| page_object        | Page Object | get_start=(Bool) | Page Object must contain 'ACTIVITY' variable with URL value if using Kwargs**| 
| page               | None        | None             |      |
| back               | None        | None             |      |
| webdriver_wait     | Number(sec) | None             |      |
| ready_state        | None        | None             |      |
| ready_state_toggle | None        | None             |      |
| get_window_size    | None        | None             |      |
| sleep              | Number(sec) | None             |      |

### citronella.Ui

###### Args:
- by
- value
- page_object (optional)

###### Method Lists:
| Method Name   | Args*  | Kwargs**           | Note |
| ------------- |:------:|:------------------:|:----:|
| send_keys     | String | clear=(Bool)       |      |
| click         | None   | switch_page=(Bool) |      |
| is_located    | None   | None               |      |
| get_attribute | String | None               |      |
| get_element   | None   | None               |      |
| get_elements  | None   | None               |      |
| text          | None   | None               |      |
