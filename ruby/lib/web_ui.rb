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

      private def webdriver_wait(ele, displayed=false)
        el = Selenium::WebDriver::Wait.new(timeout: @wait).until { ele }
        if displayed
          @wait.times do
            break if el.displayed?
            sleep(1)
          end
        end
        el
      end

      def send_keys(text, clear=false, return_key=false, switch_page=true)
        Citronella::Log.logger(@logger, @class_name, @function_name, __method__)
        el = webdriver_wait(@driver.find_element(@locator), displayed=true)
        el.send_keys text

        if return_key
          el.send_keys :return

          if @new_page and switch_page
            @pages.append(@new_page)
          end
        end
      end

      def click(switch_page=true)
        Citronella::Log.logger(@logger, @class_name, @function_name, __method__)
        el = webdriver_wait(@driver.find_element(@locator), displayed=true)
        el.click

        if @new_page and switch_page
          @pages.append(@new_page)
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
    end
  end
end
