require_relative 'logger'

module Citronella
  module Ui
    class WebUi
      def initialize(driver, webdriver_wait, pages, logger, locator, new_page,
                     function_name, class_name)
        @driver = driver
        @wait = webdriver_wait
        @pages = pages
        @logger = logger
        @locator = locator
        @new_page = new_page
        @function_name = function_name
        @class_name = class_name
      end

      private def webdriver_wait(ele, wait=nil)
        Selenium::WebDriver::Wait.new(timeout: wait ? wait : @wait).until { ele }
      end
      def send_keys(text, enter: false)
        Citronella::Log.logger(@logger, @class_name, @function_name, __method__)
        el = webdriver_wait(@driver.find_element(@locator))
        el.send_keys text

        if enter
          el.send_keys :return

          if @new_page
            @pages.get << @new_page
          end
        end
      end

      def click
        Citronella::Log.logger(@logger, @class_name, @function_name, __method__)
        el = webdriver_wait(@driver.find_element(@locator))
        webdriver_wait(el.displayed? )
        el.click

        if @new_page
          @pages.get << @new_page
        end
      end

      def get_element
        Citronella::Log.logger(@logger, @class_name, @function_name, __method__.to_s)
        webdriver_wait(@driver.find_element(@locator))
      end

      def get_elements
        Citronella::Log.logger(@logger, @class_name, @function_name, __method__.to_s)
        webdriver_wait(@driver.find_elements(@locator))
      end

      #def enabled?
      #  Citronella::Log.logger(@logger, @class_name, @function_name, __method__.to_s)
      #  webdriver_wait(@driver.find_element(@locator)).enabled?
      #end

      #def selected?
      #  Citronella::Log.logger(@logger, @class_name, @function_name, __method__.to_s)
      #  webdriver_wait(@driver.find_element(@locator)).selected?
      #end

      #def displayed?
      #  Citronella::Log.logger(@logger, @class_name, @function_name, __method__.to_s)
      #  webdriver_wait(@driver.find_element(@locator)).displayed?
      #end
    end
  end
end
