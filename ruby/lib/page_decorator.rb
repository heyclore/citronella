require_relative 'web_ui.rb'

module Citronella
  module Wrapper
    class PageDecorator
      def initialize(driver, webdriver_wait, pages, logger)
        @driver = driver
        @webdriver_wait = webdriver_wait
        @pages = pages
        @logger = logger
      end

      def method_missing(attr)
        original_method = @pages.current_page.new.method(attr)
        args = original_method.call
        Citronella::Ui::WebUi.new(@driver, @webdriver_wait, @pages, @logger,
                                  args.last, args.first, attr, @pages.current_page.name)
      end
    end
  end
end
