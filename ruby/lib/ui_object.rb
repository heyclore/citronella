module Citronella
  module UiObject
    class Ui
      def initialize(driver, webdriver_wait, pages, locator, page, exception)
        @driver = driver
        @webdriver_wait = Selenium::WebDriver::Wait.new(timeout: webdriver_wait)
        @pages = pages
        @locator = locator
        @page = page
        @exception = exception
      end

      def send_keys(text, enter: false)
        @webdriver_wait.until { @driver.find_element(@locator).displayed? }
        el = @driver.find_element(@locator)
        el.send_keys text

        if enter
          el.send_keys :return

          if @page
            @pages.get << @page
          end
        end
      end

      def click
        @webdriver_wait.until { @driver.find_element(@locator).displayed? }
        @driver.find_element(@locator).click

        if @page
          @pages.get << @page
        end
      end

      def get_elements
        @webdriver_wait.until { @driver.find_element(@locator).displayed? }
        @driver.find_elements(@locator)
      end
    end
  end
end

