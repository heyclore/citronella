# Citronella

[![PyPI version](https://badge.fury.io/py/citronella.svg)](https://badge.fury.io/py/citronella)
[![Downloads](https://pepy.tech/badge/citronella)](https://pepy.tech/project/citronella)

webdriver extension with a page object wrapper.

![alt terminal](https://github.com/heyclore/citronella/blob/main/python/screenshot/terminal.png?raw=true)
![alt pytest-html](https://github.com/heyclore/citronella/blob/main/python/screenshot/pytest_html.png?raw=true)
![alt github-action](https://github.com/heyclore/citronella/blob/main/python/screenshot/github_action.png?raw=true)

## Example Tests

### Selenium

```python
import pytest
from Pages.contents_page import ContentsPage


class TestNavigationMenu:

    def test_help_page(self, web):
        web.driver.get('https://pypi.org/')
        web.page = ContentsPage

        web.page.home_page.help_button.click()
        assert 'Help' in web.driver.title

    def test_sponsors_page(self, web):
        web.page.help_page.sponsors_button.click()
        assert 'Sponsors' in web.driver.title

    def test_login_page(self, web):
        web.page.sponsors_page.login_button.click()
        assert 'Log' in web.driver.title

    def test_register_page(self, web):
        web.page.login_page.register_button.click()
        assert 'Create' in web.driver.title
```

### Appium

```python
import pytest
from Pages.contents_page import ContentsPage


class TestInput:

    def test_input(self, web):
        web.page = ContentsPage
        web.page.home_page.gallery_button.click()
        web.page.gallery_page.text_input.send_keys('citronella')
        web.page.gallery_page.add_button.click()
        elements = web.page.gallery_page.text_lists.get_elements()
        assert 'citronella' in [x.text for x in elements]
```

Even though this module is mainly designed for the page object model, it can also be used without it for quick prototyping or mockups, etc.
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from citronella import WebPage


driver = webdriver.Chrome()

web = WebPage(driver, webdriver_wait=20, logger=False)
web.driver.get('https://pypi.org/')

web.locate(By.ID, 'search').get_element().send_keys('citronella')
web.locate(By.XPATH, '//button[@type="submit"]/i').get_element().click()

elements = web.locate(By.XPATH, '//span[@class="package-snippet__name"]')
if elements.ec_visibility_of_all_elements_located():
    results = elements.get_elements()
    text_lists = [x.text for x in results]
```

___
## Install Package

```bash
pip install citronella
```

___
## Documentation

There are only two modules import in this package:

* The first module is for conftest.py.

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

* The second module are for the page object model.

### Selenium

```python
from selenium.webdriver.common.by import By
from citronella import ui
from Pages.components import Header


class HomePage(Header):

    def some_button(self):
        return ui(By.XPATH, '//a[@name="foo"]')

    def search_input(self):
        return ui(By.ID, 'search')

    def search_button(self):
        return ui(By.NAME, 'search-button')
```

### Appium

```python
from appium.webdriver.common.appiumby import AppiumBy
from citronella import ui
from Pages.components import Header


class HomePage(Header):

    def some_button(self):
        return ui(AppiumBy.XPATH, '//a[@name="foo"]')

    def search_input(self):
        return ui(AppiumBy.ACCESSIBILITY_ID, 'search')

    def search_button(self):
        return ui(AppiumBy.ID, 'search-button')
```

___
## Page Object Design / Strategy

There's a two ways to create a page object for `WebPage`:

1. Straightforward approach: This method requires importing the page object for each test.
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from citronella import WebPage, ui


class HomePage:
    def auth_buton(self):
        return ui(By.XPATH, '//a[@name="foo"]')

class LoginPage:
    def email_input(self):
        return ui(By.ID, 'email')

    def password_input(self):
        return ui(By.ID, 'password')

    def login_buton(self):
        return ui(By.ID, 'login')

driver = webdriver.Chrome()
web = WebPage(driver)
web.driver.get('https://foobarbaz.com/')
web.page = HomePage
web.page.auth_button.click()
web.page = LoginPage
web.page.email_input.send_keys('foo')
web.page.password_input.send_keys('bar')
web.page.login_button.click()
```

2. Lazy loading approach: This method is slightly more complex but offers the benefit of lazy loading.
see [ContentsPage example](https://github.com/heyclore/citronella/blob/main/python/example/selenium/Pages/contents_page.py)
or this [Page object example](https://github.com/heyclore/citronella/tree/main/python/example/selenium/Pages)
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from citronella import WebPage, ui


class ContentsPage:
    def home_page(self):
        return HomePage

    def login_page(self):
        return LoginPage

class HomePage:
    def auth_buton(self):
        return ui(By.XPATH, '//a[@name="foo"]')

class LoginPage:
    def email_input(self):
        return ui(By.ID, 'email')

    def password_input(self):
        return ui(By.ID, 'password')

    def login_buton(self):
        return ui(By.ID, 'login')

driver = webdriver.Chrome()
web = WebPage(driver)
web.driver.get('https://foobarbaz.com/')
web.page = ContentsPage
web.page.home_page.auth_button.click()
web.page.login_page.email_input.send_keys('foo')
web.page.login_page.password_input.send_keys('bar')
web.page.login_page.login_button.click()
```

___
## Usage

### citronella.WebPage

###### Args:
- driver / webdriver

###### Kwargs (optional):
- webdriver_wait `number(seconds)`, default value is `10`
- logger `bool`, default value is `True`

###### Method Lists:
| Method Name        | Args*       | Kwargs**         | Note |
| ------------------ |:-----------:|:----------------:|:----:|
| driver             | -           | -                | return selenium `webdriver` object |
| locate             | by, value   | -                | similar as`driver.get_element` args |
| page               | page object | -                | setter |
| page               | -           | -                | getter |
| webdriver_wait     | number(sec) | -                |      |
| ready_state        | number(sec) | -                | execute javascript `document.readyState` manually, default timeout is `30` |
| sleep              | number(sec) | -                |      |

### citronella.ui / citronella.WebUi

###### Args:
- by
- value

###### Method Lists:
| Method Name   | Args*  | Kwargs**           | Note |
| ------------- |:------:|:------------------:|:----:|
| send_keys     | text   | clear `bool`, return_key `bool` |     |
| click         | -      | -                  |      |
| get_element   | -      | -                  |      |
| get_elements  | -      | -                  |      |
| ec_element_to_be_clickable | -    | -    | wrapper of `EC` / `excpected_condition` |
| ec_presence_of_element_located | -    | -    | wrapper of `EC` / `excpected_condition` |
| ec_presence_of_all_elements_located | -    | -    | wrapper of `EC` / `excpected_condition` |
| ec_visibility_of_element_located | -    | -    | wrapper of `EC` / `excpected_condition` |
| ec_visibility_of_all_elements_located | -    | -    | wrapper of `EC` / `excpected_condition` |
| ec_visibility_of_any_elements_located | -    | -    | wrapper of `EC` / `excpected_condition` |
| ec_invisibility_of_element_located | -    | -    | wrapper of `EC` / `excpected_condition` |
| ec_element_located_to_be_selected | -    | -    | wrapper of `EC` / `excpected_condition` |


## Testing powered by
<a target="_blank" href="https://www.browserstack.com/"><img width="200" src="https://www.browserstack.com/images/layout/browserstack-logo-600x315.png"></a><br>
[BrowserStack Open-Source Program](https://www.browserstack.com/open-source)
