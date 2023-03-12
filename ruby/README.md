# Citronella

[![Gem Version](https://badge.fury.io/rb/citronella.png)](http://badge.fury.io/rb/citronella)

webdriver extension with a page object wrapper.

## Example Tests
```ruby
require 'test/unit'
require "selenium-webdriver"
require 'citronella'
require_relative '../pages/contents_page'


class NavigationTest < Test::Unit::TestCase
  def setup
    options = Selenium::WebDriver::Chrome::Options.new
    driver = Selenium::WebDriver.for :chrome, options: options
    @web = Citronella::Web::WebPage.new(driver)
  end

  def teardown
    @web.driver.quit
  end

  def test_navigation
    @web.page_object(ContentsPage.new.home_page, url=true)
    @web.page.releases_button.click
    assert_includes(@web.driver.title, 'Releases')

    @web.page.gems_button.click
    assert_includes(@web.driver.title, 'Gem')
    
    @web.page.sign_in_button.click
    assert_includes(@web.driver.title, 'Sign in')
    
    @web.page.sign_up_button.click
    assert_includes(@web.driver.title, 'Sign up')
    
    @web.page.guides_button.click
    assert_includes(@web.driver.title, 'Guides')
    
    @web.page.blog_button.click
    assert_includes(@web.driver.title, 'Blog')
  end
end
```
___
## Install Package

```bash
gem install citronella
```

___
## Documentation

There are only three modules imported in this package:

* The first module is for the tests.

```ruby
require 'test/unit'
require "selenium-webdriver"
require 'citronella'

class NavigationTest < Test::Unit::TestCase
  def setup
    options = Selenium::WebDriver::Chrome::Options.new
    driver = Selenium::WebDriver.for :chrome, options: options
    @web = Citronella::Web::WebPage.new(driver)
  end

  def teardown
    @web.driver.quit
  end
end
```

* The second and third modules are for the page object model.

```python
require 'citronella'
require_relative '../contents_page'

class HomePage < ContentsPage.new.header_menu
  @url = "https://rubygems.org/"

  def search_button
    ui(class: 'home__search__icon', page: ContentsPage.new.search_page)
  end

  def code_link_button
    ui(css: 'div.nav--v > a:nth-child(3)', page: Citronella::Dummy::PlaceholderPage)
  end
end
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
| driver             | None        | None             | return selenium `webdriver` object |
| locate             | by, value   | None             | similar as`driver.get_element` args |
| page_object        | Page Object | get_start `bool` | Page Object must contain `ACTIVITY` variable with URL(selenium)/State(appium) if using Kwargs** | 
| page               | None        | None             |      |
| back               | None        | None             |      |
| webdriver_wait     | number(sec) | None             |      |
| ready_state        | number(sec) | None             | execute javascript `document.readyState` manually, default timeout is `0` |
| get_window_size    | None        | None             |      |
| sleep              | number(sec) | None             |      |

### citronella.ui / citronella.WebUi

###### Args:
- by
- value
- page_object (optional)

###### Method Lists:
| Method Name   | Args*  | Kwargs**           | Note |
| ------------- |:------:|:------------------:|:----:|
| send_keys     | text   | clear `bool`, return_key `bool` | default value is `False` by default |
| click         | None   | switch_page `bool` | see [test_auth.py](example/selenium/Test/pytest_html_image/test_auth.py) example |
| get_element   | None   | None               |      |
| get_elements  | None   | None               |      |
| ec_element_to_be_clickable | None | None | wrapper of `EC` / `excpected_condition` |
| ec_presence_of_element_located | None | None | wrapper of `EC` / `excpected_condition` |
| ec_presence_of_all_elements_located | None | None | wrapper of `EC` / `excpected_condition` |
| ec_visibility_of_element_located | None | None | wrapper of `EC` / `excpected_condition` |
| ec_visibility_of_all_elements_located | None | None | wrapper of `EC` / `excpected_condition` |
| ec_visibility_of_any_elements_located | None | None | wrapper of `EC` / `excpected_condition` |
| ec_invisibility_of_element_located | None | None | wrapper of `EC` / `excpected_condition` |
| ec_element_located_to_be_selected | None | None | wrapper of `EC` / `excpected_condition` |


## Testing powered by
<a target="_blank" href="https://www.browserstack.com/"><img width="200" src="https://www.browserstack.com/images/layout/browserstack-logo-600x315.png"></a><br>
[BrowserStack Open-Source Program](https://www.browserstack.com/open-source)
