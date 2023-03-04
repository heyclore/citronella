require "selenium-webdriver"
require_relative '../lib/citronella'

class Component
  def search_input
    ui(id: 'home_query', page: SearchPage)
  end

end

class HomePage < Component
  def search_button
    ui(class: 'home__search__icon', page: SearchPage)
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
web.back
puts web.page.search_button.enabled?
puts web.page.search_button.selected?
puts web.page.search_button.displayed?
web.page.search_button.get_element.click
web.back
web.locate(id: 'home_query').get_element.clear
web.locate(id: 'home_query').get_element.send_keys('citronella')
web.locate(class: 'home__search__icon').get_element.click
web.driver.quit
