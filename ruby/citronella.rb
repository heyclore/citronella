#Ui
module Citronella
  module UiWrapper
    class Ui
      def initialize(driver, webdriver_wait, pages, locator)
        @driver = driver
        @webdriver_wait = webdriver_wait
        @pages = pages
        @locator = locator.first
        @page = locator.last
      end

      def get_elements
        puts :get_elements
      end

      def click
        puts :click
        if @page
          @pages.get << @page
        end
      end

      def text
        puts :text
      end
    end
  end
end

#page_decorator
module Citronella
  module Decorator
    def self.method_wrapper(klass, method_name, driver, webdriver_wait, pages)
      original_method = klass.instance_method(method_name)
      klass.define_method(method_name) do
        puts method_name
        locator = original_method.bind(self).call
        Citronella::UiWrapper::Ui.new(driver, webdriver_wait, pages, locator)
      end
    end

    def self.class_decorator(klass, driver, webdriver_wait, pages)
      return if klass.instance_variable_defined?(:@decorated)
      klass.instance_variable_set(:@decorated, true)
      return if klass.name == "Object"
      lists = klass.instance_methods(false)
      lists.each { |method| method_wrapper(klass, method, driver, webdriver_wait, pages) }
      class_decorator(klass.superclass, driver, webdriver_wait, pages)
    end

    def self.page_decorator(driver, webdriver_wait, pages)
      klass = pages.get.last
      class_decorator(klass, driver, webdriver_wait, pages)
      klass.new
    end
  end
end

#Pages
module Citronella
  module Pages
    class PagesList
      def initialize
        @page_lists = []
      end

      def get
        if @page_lists.length > 5
          @page_lists.shift
        end
        @page_lists
      end
    end
  end
end

#WebPage
module Citronella
  class WebPage
    def initialize(driver, webdriver_wait=10000)
      @driver = driver
      @webdriver_wait = webdriver_wait
      @pages = Citronella::Pages::PagesList.new
    end

    def driver
      @driver
    end

    def page_object(x)
      @pages.get << x
    end

    def page
      Citronella::Decorator.page_decorator(@driver, @webdriver_wait, @pages)
    end
  end
end

def ui(x,y=nil)
  [x,y]
end
