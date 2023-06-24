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
    @web.page = ContentsPage
    @web.driver.navigate.to('https://rubygems.org')
  end

  def teardown
    @web.driver.quit
  end

  def test_navigation
    @web.page.home_page.releases_button.click
    assert_includes(@web.driver.title, 'Releases')

    @web.page.release_page.gems_button.click
    assert_includes(@web.driver.title, 'Gem')
    
    @web.page.gems_page.sign_in_button.click
    assert_includes(@web.driver.title, 'Sign in')
    
    @web.page.sign_in_page.sign_up_button.click
    assert_includes(@web.driver.title, 'Sign up')
    
    @web.page.sign_up_page.guides_button.click
    assert_includes(@web.driver.title, 'Guides')
    
    @web.page.guides_page.blog_button.click
    assert_includes(@web.driver.title, 'Blog')
  end
end
```
![alt terminal](https://github.com/heyclore/citronella/blob/main/ruby/screenshot/terminal.png?raw=true)

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
    @web.locate(id: 'home_query').send_keys('citronella')
    @web.locate(class: 'home__search__icon').click
    assert(@web.locate(class: 'gems__gem__name').get_element.text, 'citronella')
  end
end
```
![alt terminal](https://github.com/heyclore/citronella/blob/main/ruby/screenshot/terminal2.png?raw=true)

___
## Install Package

```bash
gem install citronella
```

___
## Documentation

There are only two modules imported in this package:

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

* The last module is for the page object model.

```ruby
require 'citronella'
require_relative '../components/header_menu'

class HomePage
  include HeaderMenu

  def search_button
    ui(class: 'home__search__icon')
  end

  def code_link_button
    ui(css: 'div.nav--v > a:nth-child(3)')
  end
end
```

___
## Page Object Design / Strategy
see full [Page object](https://github.com/heyclore/citronella/tree/main/ruby/examples/page_object/pages) example
```ruby
require "selenium-webdriver"
require 'citronella'

module HeaderMenu
  def home_logo
    ui(class: 'header__logo')
  end

  def search_input
    ui(id: 'home_query')
  end
  
  def gems_button
    ui(css: 'a[href="/gems"]')
  end
end

class HomePage
  include HeaderMenu

  def search_button
    ui(class: 'home__search__icon')
  end

  def code_link_button
    ui(css: 'div.nav--v > a:nth-child(3)')
  end
end

class SearchPage
  include HeaderMenu

  def search_lists
    ui(class: 'gems__gem__name')
  end
end

class ContentsPage
  def home_page
    HomePage
  end

  def search_page
    SearchPage
  end
end

options = Selenium::WebDriver::Chrome::Options.new
driver = Selenium::WebDriver.for :chrome, options: options
web = Citronella::Web::WebPage.new(driver)
web.page = ContentsPage
web.driver.navigate.to('https://rubygems.org')
web.page.home_page.search_input.send_keys('citronella', return_key=true)
puts web.page.search_page.search_list.get_element.text
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
| driver             | -           | -                | return selenium `webdriver` object |
| locate             | -           | how: what        | similar as`driver.get_element` as input & return [citronella.WebUi](https://github.com/heyclore/citronella/tree/main/ruby#citronellaui--citronellawebui)|
| page               | Page Object | -                | setter |
| page               | -           | -                | getter |
| webdriver_wait     | number(sec) | -                |      |
| ready_state        | number(sec) | -                | execute javascript `document.readyState` manually |

### citronella.ui / citronella.WebUi

###### Kwargs:
- how: what

###### Method Lists:
| Method Name   | Args*  | Kwargs**           | Note |
| ------------- |:------:|:------------------:|:----:|
| send_keys     | text   | clear `bool`, return_key `bool` |      |
| click         | -      | -                  |      |
| get_element   | -      | -                  |      |
| get_elements  | -      | -                  |      |


## Testing powered by
<a target="_blank" href="https://www.browserstack.com/"><img width="200" src="https://www.browserstack.com/images/layout/browserstack-logo-600x315.png"></a><br>
[BrowserStack Open-Source Program](https://www.browserstack.com/open-source)
