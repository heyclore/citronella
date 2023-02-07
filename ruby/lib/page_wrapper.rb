require_relative 'ui_object.rb'

module Citronella
  module PageWrapper
    def self.method_wrapper(klass, method_name, driver, webdriver_wait, pages)
      original_method = klass.instance_method(method_name)
      klass.define_method(method_name) do
        puts method_name
        args = original_method.bind(self).call
        Citronella::UiObject::Ui.new(driver, webdriver_wait, pages,
                                      args.locator, args.page, args.exception)
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

    def self.ui_decorator(driver, webdriver_wait, pages)
      klass = pages.get.last
      class_decorator(klass, driver, webdriver_wait, pages)
      klass.new
    end
  end
end
