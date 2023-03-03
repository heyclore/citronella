require_relative 'page_tab'
require_relative 'page_decorator'

module Citronella
  module Web
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

      def page_object(new_page)
        @pages.get << new_page
      end

      def page
        Citronella::Wrapper::PageDecorator.new(@driver, @webdriver_wait, @pages, @logger)
      end

      def locate
      end

      def back
        driver.navigate.back
        @pages.get.delete_at(-1)
      end

      def ready_state(wait)
        wait.times do |i|
          return if driver.execute_script("return document.readyState") == "complete"
          sleep(1)
        end
      end

      def webdriver_wait
      end
    end
  end
end
