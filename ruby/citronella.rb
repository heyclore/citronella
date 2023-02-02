#Ui
module Citronella
  module UiWrapper
    class Ui
      def initialize(driver, webdriver_wait, pages, locator)
        @driver = driver
        @webdriver_wait = webdriver_wait
        @pages = pages
        @locator = locator[0]
        @page = locator[1]
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
    def self.wrapper(cls, method_name, driver, webdriver_wait, pages)
      #if cls.respond_to?(method_name)
      #  puts :raise
      #  return
      #end
      original_method = cls.instance_method(method_name)
      cls.define_method(method_name) do
        puts method_name
        locator = original_method.bind(self).call
        Citronella::UiWrapper::Ui.new(driver, webdriver_wait, pages, locator)
      end
    end

    def self.page_decorator(driver, webdriver_wait, pages)
      cls = pages.get.last
      return cls.new if cls.instance_variable_defined?(:@decorated)
      cls.instance_variable_set(:@decorated, true)

      lists = cls.instance_methods(false)
      #lists.each { |method| wrapper(cls, method, driver, webdriver_wait, pages) }
      for method in lists
        wrapper(cls, method, driver, webdriver_wait, pages)
      end
      cls.new
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
