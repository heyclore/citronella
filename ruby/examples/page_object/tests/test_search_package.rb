require 'test/unit'
require "selenium-webdriver"
require_relative '../../../lib/citronella'
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


class NavigationAlternativeTest < Test::Unit::TestCase
  def setup
    options = Selenium::WebDriver::Chrome::Options.new
    driver = Selenium::WebDriver.for :chrome, options: options
    @web = Citronella::Web::WebPage.new(driver)
    @web.page_object(ContentsPage.new.home_page, url=true)
  end

  def teardown
    @web.driver.quit
  end

  def test_release_page
    @web.page.releases_button.click
    assert_includes(@web.driver.title, 'Releases')
  end

  def test_gem_page
    @web.page.gems_button.click
    assert_includes(@web.driver.title, 'Gem')
  end
    
  def test_sign_in_page
    @web.page.sign_in_button.click
    assert_includes(@web.driver.title, 'Sign in')
  end
    
  def test_sign_up_page
    @web.page.sign_up_button.click
    assert_includes(@web.driver.title, 'Sign up')
  end
    
  def test_guides_page
    @web.page.guides_button.click
    assert_includes(@web.driver.title, 'Guides')
  end
    
  def test_blog_page
    @web.page.blog_button.click
    assert_includes(@web.driver.title, 'Blog')
  end
end


class AnotherNavigationAlternativeTest < Test::Unit::TestCase
  self.test_order = :defined

  def self.startup
    options = Selenium::WebDriver::Chrome::Options.new
    driver = Selenium::WebDriver.for :chrome, options: options
    @@web = Citronella::Web::WebPage.new(driver)
  end

  def self.shutdown
    @@web.driver.quit
  end

  def test_release_button_page
    @@web.page_object(ContentsPage.new.home_page, url=true)
    @@web.page.releases_button.click
    assert_includes(@@web.driver.title, 'Releases')
  end

  def test_gems_page
    @@web.page.gems_button.click
    assert_includes(@@web.driver.title, 'Gem')
  end

  def test_sign_in_page
    @@web.page.sign_in_button.click
    assert_includes(@@web.driver.title, 'Sign in')
  end

  def test_sign_up_page
    @@web.page.sign_up_button.click
    assert_includes(@@web.driver.title, 'Sign up')
  end

  def test_guides_page
    @@web.page.guides_button.click
    assert_includes(@@web.driver.title, 'Guides')
  end

  def test_blog_page
    @@web.page.blog_button.click
    assert_includes(@@web.driver.title, 'Blog')
  end
end
