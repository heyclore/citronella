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
      """This is a page decorator class."""
      def initialize(driver, webdriver_wait, page, logger)
        @driver = driver
        @webdriver_wait = webdriver_wait
        @page = page
        @logger = logger
      end

      def method_missing(attr)
        """look up the attr / method name inside page object."""
        original_method = @page.new.method(attr)
        args = original_method.call
        if args.instance_of?(Class)
          return PageDecorator.new(@driver, @webdriver_wait, args, @logger)
        end
        Citronella::Ui::WebUi.new(@driver, @webdriver_wait, @logger,
                                  args.last, attr, @page.name)
      end
    end
  end
end
