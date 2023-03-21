# Citronella

[![Gem Version](https://badge.fury.io/rb/citronella.svg)](http://badge.fury.io/rb/citronella)

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
Even though this module is mainly designed for the page object model, it can also be used without it for quick prototyping or mockups, etc.
```ruby
require 'test/unit'
require "selenium-webdriver"
require 'citronella'


class PackageSearchTest < Test::Unit::TestCase
  def setup
    options = Selenium::WebDriver::Chrome::Options.new
    driver = Selenium::WebDriver.for :chrome, options: options
    @web = Citronella::Web::WebPage.new(driver)
  end

  def teardown
    @web.driver.quit
  end

  def test_search_package
    @web.driver.navigate.to "https://rubygems.org/"
    @web.locate(id: 'home_query').get_element.send_keys('citronella')
    @web.locate(class: 'home__search__icon').get_element.click
    assert(@web.locate(class: 'gems__gem__name').get_element.text, 'citronella')
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
- logger `bool`, default value is `true`

###### Method Lists:
| Method Name        | Args*       | Kwargs**         | Note |
| ------------------ |:-----------:|:----------------:|:----:|
| driver             | None        | None             | return selenium `webdriver` object |
| locate             | None        | how: what        | similar as`driver.get_element` args |
| page_object        | Page Object | url `bool`       | Page Object must contain `@url` variable with if using Kwargs** | 
| page               | None        | None             |      |
| back               | None        | None             |      |
| webdriver_wait     | number(sec) | None             |      |
| ready_state        | number(sec) | None             | execute javascript `document.readyState` manually |

### citronella.ui / citronella.WebUi

###### Kwargs:
- how: what
- page_object (optional)

###### Method Lists:
| Method Name   | Args*  | Kwargs**           | Note |
| ------------- |:------:|:------------------:|:----:|
| send_keys     | text   | clear `bool`, return_key `bool`, switch_page `bool` |    |
| click         | None   | switch_page `bool` |      |
| get_element   | None   | None               |      |
| get_elements  | None   | None               |      |


## Testing powered by
<a target="_blank" href="https://www.browserstack.com/"><img width="200" src="https://www.browserstack.com/images/layout/browserstack-logo-600x315.png"></a><br>
[BrowserStack Open-Source Program](https://www.browserstack.com/open-source)
