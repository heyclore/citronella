require_relative 'page_tab'
require_relative 'page_decorator'

module Citronella
  class WebPage
    def initialize(driver, webdriver_wait:10, logger:true)
      @driver = driver
      @webdriver_wait = webdriver_wait
      @pages = Citronella::PagesList.new
      @logger = logger
    end

    def driver
      @driver
    end

    def page_object(x)
      @pages.get << x
    end

    def page
      Citronella::PageDecorator.new(@driver, @webdriver_wait, @pages, @logger)
    end
  end
end
