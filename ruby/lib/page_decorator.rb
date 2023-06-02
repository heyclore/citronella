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


require_relative 'web_ui.rb'

module Citronella
  module Wrapper
    class PageDecorator
      # A wrapper for page object class.
      #
      # @param [Webdriver] driver The web driver object.
      # @param [Integer] webdriver_wait The timeout for webdriver wait.
      # @param [PageObject] page The page object class.
      # @param [Boolean] logger A flag indicating whether to log actions.
      #
      def initialize(driver, webdriver_wait, page, logger)
        @driver = driver
        @webdriver_wait = webdriver_wait
        @page = page
        @logger = logger
      end

      # Looks up the attribute/method name inside the page object.
      #
      # @return [PageDecorator, WebUi]
      #
      def method_missing(attr)
        original_method = @page.new.method(attr)
        args = original_method.call
        if args.instance_of?(Class)
          return PageDecorator.new(@driver, @webdriver_wait, args, @logger)
        end
        Citronella::Ui::WebUi.new(@driver, @webdriver_wait, @logger,
                                  args, attr, @page.name)
      end
    end
  end
end
