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
      """a wrapped object of a web element."""
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
        """return a web element or elements."""
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
        """custom webdriver send_keys with optional clear field."""
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
        """click to web element."""
        Citronella::Log.logger(@logger, @class_name, @function_name, __method__)
        el = webdriver_wait(@driver.find_element(@locator), displayed=true)
        el.click

        if @new_page and switch_page
          @pages.append(@new_page)
        end
      end

      def get_element
        """return web element, equal as find_element."""
        Citronella::Log.logger(@logger, @class_name, @function_name, __method__.to_s)
        webdriver_wait(@driver.find_element(@locator))
      end

      def get_elements
        """return list of web element, equal as find_elements."""
        Citronella::Log.logger(@logger, @class_name, @function_name, __method__.to_s)
        webdriver_wait(@driver.find_elements(@locator))
      end
    end
  end
end
