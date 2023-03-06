require_relative 'page_tab'
require_relative 'page_decorator'
require_relative 'web_ui'

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

      def page_object(new_page, url=false)
        if url
          if not new_page.instance_variable_get(:@url)
            raise "Error: '@url' variable does not exist in #{new_page}"
          end
          @driver.navigate.to(new_page.instance_variable_get(:@url))
        end
        @pages.get << new_page
      end

      def page
        Citronella::Wrapper::PageDecorator.new(@driver, @webdriver_wait, @pages, @logger)
      end

      def locate(args)
        Citronella::Ui::WebUi.new(@driver, @webdriver_wait, @pages, @logger, args, nil,
                                  __method__.to_s, self.class.name.split('::').last.to_s)
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

      def webdriver_wait(wait)
        puts @webdriver_wait
        @webdriver_wait = wait
        puts @webdriver_wait
      end
    end
  end
end
