require_relative 'web_ui.rb'

module Citronella
  class PageDecorator
    def initialize(driver, webdriver_wait, pages, logger)
      @driver = driver
      @webdriver_wait = webdriver_wait
      @pages = pages
      @logger = logger
    end

    def method_missing(attr)
      original_method = @pages.get.last.new.method(attr)
      args = original_method.call
      Citronella::WebUi.new(@driver, @webdriver_wait, @pages, @logger,
                            args.locator, args.page, attr, @pages.get.last.name)
    end
  end
end
