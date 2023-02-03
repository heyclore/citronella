require "selenium-webdriver"
require_relative 'citronella.rb'

class Component
  def search_input
    ui(id: 'home_query', page: SearchPage)
  end

end

class HomePage < Component
  def search_button
    ui(css: 'input[type="submit"]', page: SearchPage , exception: :foo)
  end
end

class SearchPage < Component
  def search_lists
    ui(class: 'gems__gem__name')
  end
end

options = Selenium::WebDriver::Chrome::Options.new
#options.add_argument('--headless')
driver = Selenium::WebDriver.for :chrome, options: options


web = Citronella::WebPage.new(driver)
web.page_object HomePage
web.driver.navigate.to "https://rubygems.org/"
web.page.search_input.send_keys('selenium', enter: true)
lists = web.page.search_lists.get_elements
for x in lists
  puts x.text
end
web.driver.quit
