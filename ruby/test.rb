require "selenium-webdriver"
require_relative 'citronella.rb'

class Component
  def search_input
    ui([name: 'q'], SearchPage)
  end

end

class HomePage < Component
  def search_button
    ui([css: 'button[type="submit"]'], SearchPage)
  end
end

class SearchPage < Component
  def search_lists
    ui([css: 'a[target="_self"]'], SearchPage)
  end
end

options = Selenium::WebDriver::Chrome::Options.new
#options.add_argument('--headless')
driver = Selenium::WebDriver.for :chrome, options: options


web = Citronella::WebPage.new(driver)
web.page_object HomePage
web.driver.navigate.to "https://www.npmjs.com/"
web.page.search_input.send_keys 'selenium'
web.page.search_button.click
lists = web.page.search_lists.get_elements
for x in lists
  puts x.text
end
web.driver.quit
