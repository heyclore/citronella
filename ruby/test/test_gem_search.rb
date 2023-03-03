require "selenium-webdriver"
require_relative '../lib/citronella'

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


web = Citronella::Web::WebPage.new(driver)
web.page_object HomePage
web.driver.navigate.to "https://rubygems.org/"
web.page.search_input.send_keys('selenium', enter: true)
web.ready_state(20)
lists = web.page.search_lists.get_elements
for x in lists
  puts x.text
end
web.back
web.page.search_input.send_keys('', enter: true)
lists = web.page.search_lists.get_elements
web.driver.quit
