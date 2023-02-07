require_relative 'page_store'
require_relative 'page_wrapper'

module Citronella
  class WebPage
    def initialize(driver, webdriver_wait=10)
      @driver = driver
      @webdriver_wait = webdriver_wait
      @pages = Citronella::PagesStore::PagesList.new
    end

    def driver
      @driver
    end

    def page_object(x)
      @pages.get << x
    end

    def page
      Citronella::PageWrapper.ui_decorator(@driver, @webdriver_wait, @pages)
    end
  end
end
