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


require_relative 'page_decorator'
require_relative 'web_ui'

module Citronella
  module Web
    class WebPage
      """
      an object class that use across the tests.
      webdriver_wait is set '10' seconds by default
      logger is set 'True' by default

      Args:
          driver
      Kwargs (optional):
          webdriver_wait
          logger

      Usage:
          driver = Selenium::WebDriver.for :chrome
          web = WebPage(driver)
      """
      def initialize(driver, webdriver_wait:10, logger:true)
        @driver = driver
        @webdriver_wait = webdriver_wait
        @page = nil
        @logger = logger
      end

      def driver
        """return the original selenium / appium driver."""
        @driver
      end

      def page
        """return last page object model."""
        Citronella::Wrapper::PageDecorator.new(@driver, @webdriver_wait, @page,
                                               @logger)
      end

      def page=(page)
        @page = page
      end

      def locate(args)
        """
        an alternative way for testing without page object and return WebUi
        class, but can't use page and back method and causing an error.
        good for quick prototype / write a tests.

        Args:
            by
            value

        Usage:
            web.ui(name: 'q').get_element.text
            web.ui(name: 'q').get_element.click
        """
        Citronella::Ui::WebUi.new(@driver, @webdriver_wait, @logger, args,
                                  __method__.to_s,
                                  self.class.name.split('::').last.to_s)
      end

      def ready_state(wait)
        """execute javascript for page to fully load"""
        wait.times do |i|
          return if driver.execute_script(
            "return document.readyState") == "complete"
          sleep(1)
        end
      end

      def webdriver_wait(wait)
        """override webdriver wait."""
        @webdriver_wait = wait
      end
    end
  end
end
