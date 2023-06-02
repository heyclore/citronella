#MIT License
#
#Copyright (c) 2023 Eko Purnomo
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


require_relative 'logger'

module Citronella
  module Ui
    class WebUi
      #
      # @param [Webdriver] driver The web driver object.
      # @param [Integer] webdriver_wait The timeout for webdriver wait.
      # @param [Boolean] logger A flag indicating whether to log actions.
      # @param [Hash] locator The locator for the web element.
      # @param [String] function_name The name of the function.
      # @param [String] class_name The name of the class.
      #
      def initialize(driver, webdriver_wait, logger, locator, function_name,
                     class_name)
        @driver = driver
        @wait = webdriver_wait
        @logger = logger
        @locator = locator
        @function_name = function_name
        @class_name = class_name
      end

      # Waits for a web element to be available and returns it.
      #
      # @param [Webdriver] ele The web driver object.
      # @param [Boolean] displayed Flag indicating whether to wait for the element to be displayed.
      # @return [Webdriver::Element] The web element.
      #
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

      # Sends keys to the web element.
      #
      # @param [String] text The text to be sent.
      # @param [Boolean] clear Flag indicating whether to clear the field before sending keys.
      # @param [Boolean] return_key Flag indicating whether to send a return key.
      #
      def send_keys(text, clear=false, return_key=false)
        Citronella::Log.logger(@logger, @class_name, @function_name, __method__)
        el = webdriver_wait(@driver.find_element(@locator), displayed=true)
        el.send_keys text

        if return_key
          el.send_keys :return
        end
      end

      # Clicks on the web element.
      #
      def click
        Citronella::Log.logger(@logger, @class_name, @function_name, __method__)
        el = webdriver_wait(@driver.find_element(@locator), displayed=true)
        el.click
      end

      # Returns a web element using find_element method.
      #
      # @return [Webdriver::Element] The web element.
      #
      def get_element
        Citronella::Log.logger(@logger, @class_name, @function_name,
                               __method__.to_s)
        webdriver_wait(@driver.find_element(@locator))
      end

      # Returns a list of web elements using find_elements method.
      #
      # @return [Array<Webdriver::Element>] The list of web elements.
      #
      def get_elements
        Citronella::Log.logger(@logger, @class_name, @function_name,
                               __method__.to_s)
        webdriver_wait(@driver.find_elements(@locator))
      end
    end
  end
end
