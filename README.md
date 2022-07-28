# Citronella

[![PyPI version](https://badge.fury.io/py/citronella.svg)](https://badge.fury.io/py/citronella)
[![Downloads](https://pepy.tech/badge/citronella)](https://pepy.tech/project/citronella)

Citronella is a selenium and/or appium webdriver extension with page object wrapper for create a tests a bit simple.

## Example Test

### Selenium

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

### Appium

```python
import pytest
from Pages.api_demos_page import ApiDemosPage


class TestNavigationMenu:

    def test_accessibility_page(self):
        self.web.page_object(ApiDemosPage)

        self.web.page.accessibility_button.click()
        assert self.web.page.accessibility_node_provider_button.get_element().is_visible()

    def test_animation_page(self):
        self.web.back
        self.web.page.animation_button.click()
        assert self.web.page.cloning_button.get_element().is_visible()

    def test_app_page(self):
        self.web.back
        self.web.page.app_button.click()
        assert self.web.page.activity_button.get_element().is_visible()

    def test_os_page(self):
        self.web.back
        self.web.page.os_button.click()
        assert self.web.page.morse_code_button.get_element().is_visible()
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
def browser(request):
    driver = webdriver.Chrome()
    web = WebPage(driver)
    request.cls.web = web
    yield
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
def init_driver(request):
    options = UiAutomator2Options()
    options.platformName = 'Android'
    options.app = os.getcwd() + '/APK/ApiDemos-debug.apk.zip'
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
    web = WebPage(driver)
    request.cls.web = web
    yield
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
| Method Name       | Selenium      | Appium  |
| ------------------ |:-------------:| -----:|
| driver             | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/selenium/Tests/test_usage_demo.py#L13)| [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/appium/Tests/test_usage_demo.py#L13) |
| page_object        | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/selenium/Tests/test_usage_demo.py#L21) | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/appium/Tests/test_usage_demo.py#L20) |
| page               | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/selenium/Tests/test_usage_demo.py#L35) | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/appium/Tests/test_usage_demo.py#L35) |
| back               | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/selenium/Tests/test_usage_demo.py#L42) | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/appium/Tests/test_usage_demo.py#L45) |
| webdriver_wait     | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/selenium/Tests/test_usage_demo.py#L50) | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/appium/Tests/test_usage_demo.py#L53) |
| ready_state        | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/selenium/Tests/test_usage_demo.py#L56) | disabled |
| ready_state_toggle | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/selenium/Tests/test_usage_demo.py#L63) | disabled |
| get_window_size    | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/selenium/Tests/test_usage_demo.py#L69) | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/appium/Tests/test_usage_demo.py#L59) |
| sleep              | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/selenium/Tests/test_usage_demo.py#L76) | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/appium/Tests/test_usage_demo.py#L66) |

### citronella.Ui

###### Args:
- by
- value
- page_object (optional)

###### Method Lists:
| Method Name       | Selenium      | Appium  |
| ------------------ |:-------------:| -----:|
| send_keys          | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/selenium/Tests/test_usage_demo.py#L86)| [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/appium/Tests/test_usage_demo.py#L79) |
| click              | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/selenium/Tests/test_usage_demo.py#L95) | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/appium/Tests/test_usage_demo.py#L89) |
| is_located         | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/selenium/Tests/test_usage_demo.py#L103) | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/appium/Tests/test_usage_demo.py#L97) |
| get_attribute      | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/selenium/Tests/test_usage_demo.py#L109) | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/appium/Tests/test_usage_demo.py#L103) |
| get_element        | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/selenium/Tests/test_usage_demo.py#L118) | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/appium/Tests/test_usage_demo.py#L111) |
| get_elements       | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/selenium/Tests/test_usage_demo.py#L124) | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/appium/Tests/test_usage_demo.py#L117) |
| text               | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/selenium/Tests/test_usage_demo.py#L130) | [example](https://github.com/heyclore/citronella/blob/82d8a46f8ef7976a1f5e796783644343470714d3/example/appium/Tests/test_usage_demo.py#L123) |
