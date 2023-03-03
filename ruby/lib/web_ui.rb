require_relative 'logger'

module Citronella
  module Ui
    class WebUi
      def initialize(driver, webdriver_wait, pages, logger, locator, new_page,
                     function_name, class_name)
        @driver = driver
        @webdriver_wait = Selenium::WebDriver::Wait.new(timeout: webdriver_wait)
        @pages = pages
        @logger = logger
        @locator = locator
        @new_page = new_page
        @function_name = function_name
        @class_name = class_name
      end

      def send_keys(text, enter: false)
        Citronella::Log.logger(@logger, @class_name, @function_name, __method__)
        @webdriver_wait.until { @driver.find_element(@locator).displayed? }
        el = @driver.find_element(@locator)
        el.send_keys text

        if enter
          el.send_keys :return

          if @new_page
            @pages.get << @new_page
          end
        end
      end

      def click
        @webdriver_wait.until { @driver.find_element(@locator).displayed? }
        @driver.find_element(@locator).click

        if @new_page
          @pages.get << @new_page
        end
      end

      def get_elements
        @webdriver_wait.until { @driver.find_element(@locator).displayed? }
        @driver.find_elements(@locator)
      end
    end
  end
end
