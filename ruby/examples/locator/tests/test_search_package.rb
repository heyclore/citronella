require 'test/unit'
require "selenium-webdriver"
require_relative '../../../lib/citronella'


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