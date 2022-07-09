# Citronella

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
## Usage

### citronella.WebPage

###### Args:
- webdriver

###### Method Lists:
- [driver](https://github.com/heyclore/citronella/blob/9ed18b33fc87beb59c8fe92768ce3ec7c5a40f29/example/Tests/test_usage_demo.py#L13)
- [page_object](https://github.com/heyclore/citronella/blob/9ed18b33fc87beb59c8fe92768ce3ec7c5a40f29/example/Tests/test_usage_demo.py#L21)
- [page](https://github.com/heyclore/citronella/blob/9ed18b33fc87beb59c8fe92768ce3ec7c5a40f29/example/Tests/test_usage_demo.py#L29)
- [back](https://github.com/heyclore/citronella/blob/9ed18b33fc87beb59c8fe92768ce3ec7c5a40f29/example/Tests/test_usage_demo.py#L36)
- [get_window_size](https://github.com/heyclore/citronella/blob/9ed18b33fc87beb59c8fe92768ce3ec7c5a40f29/example/Tests/test_usage_demo.py#L45)
- [ready_state](https://github.com/heyclore/citronella/blob/9ed18b33fc87beb59c8fe92768ce3ec7c5a40f29/example/Tests/test_usage_demo.py#L54)
- [sleep](https://github.com/heyclore/citronella/blob/9ed18b33fc87beb59c8fe92768ce3ec7c5a40f29/example/Tests/test_usage_demo.py#L60)

### citronella.Ui

###### Args:
- selenium_by
- string_locator
- new_page_object

###### Method Lists:
- [send_keys](https://github.com/heyclore/citronella/blob/9ed18b33fc87beb59c8fe92768ce3ec7c5a40f29/example/Tests/test_usage_demo.py#L70)
- [click](https://github.com/heyclore/citronella/blob/9ed18b33fc87beb59c8fe92768ce3ec7c5a40f29/example/Tests/test_usage_demo.py#L79)
- [get_attribute](https://github.com/heyclore/citronella/blob/9ed18b33fc87beb59c8fe92768ce3ec7c5a40f29/example/Tests/test_usage_demo.py#L87)
- [get_element](https://github.com/heyclore/citronella/blob/9ed18b33fc87beb59c8fe92768ce3ec7c5a40f29/example/Tests/test_usage_demo.py#L96)
- [get_elements](https://github.com/heyclore/citronella/blob/9ed18b33fc87beb59c8fe92768ce3ec7c5a40f29/example/Tests/test_usage_demo.py#L102)
- [text](https://github.com/heyclore/citronella/blob/9ed18b33fc87beb59c8fe92768ce3ec7c5a40f29/example/Tests/test_usage_demo.py#L109)
