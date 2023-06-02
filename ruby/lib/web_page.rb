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
    # An object class that is used across the tests.
    # `webdriver_wait` is set to '10' seconds by default.
    # `logger` is set to 'true' by default.
    #
    # @param [Webdriver] driver The web driver object.
    # @param [Integer] webdriver_wait The timeout for webdriver wait.
    # @param [Boolean] logger A flag indicating whether to log actions.
    #
    # Usage:
    #   driver = Selenium::WebDriver.for :chrome
    #   web = WebPage.new(driver)
    #
    class WebPage
      def initialize(driver, webdriver_wait:10, logger:true)
        @driver = driver
        @webdriver_wait = webdriver_wait
        @page = nil
        @logger = logger
      end

      # Returns the original Selenium driver.
      #
      # @return [Webdriver] The web driver object.
      #
      def driver
        @driver
      end

      # Returns the wrapped page object model.
      #
      # @return [Citronella::Wrapper::PageDecorator] The page object model.
      #
      def page
        Citronella::Wrapper::PageDecorator.new(@driver, @webdriver_wait, @page,
                                               @logger)
      end

      # Sets the page object model.
      #
      # @param [PageObject] page The page object model.
      #
      def page=(page)
        @page = page
      end

      # An alternative way for testing without using page objects.
      # It returns a WebUi class, but can't use `page` and may cause an error.
      # It's good for quick prototypes or writing tests.
      #
      # @param [Hash] args The locator details.
      # @return [Citronella::Ui::WebUi] The web element.
      #
      # Usage:
      #   web.ui(name: 'q').get_element.text
      #   web.ui(name: 'q').get_element.click
      #
      def locate(args)
        Citronella::Ui::WebUi.new(@driver, @webdriver_wait, @logger, args,
                                  __method__.to_s,
                                  self.class.name.split('::').last.to_s)
      end

      # Executes JavaScript to wait for the page to fully load.
      #
      # @param [Integer] wait The number of times to check the page's ready state.
      #
      def ready_state(wait)
        wait.times do |i|
          return if driver.execute_script(
            "return document.readyState") == "complete"
          sleep(1)
        end
      end

      # Overrides the `webdriver_wait` value.
      #
      # @param [Integer] wait The new value for `webdriver_wait`.
      #
      def webdriver_wait(wait)
        @webdriver_wait = wait
      end
    end
  end
end
