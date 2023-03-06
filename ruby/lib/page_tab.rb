module Citronella
  class PagesList
    def initialize
      @pages = []
    end

    def current_page
      @pages.last
    end

    def append(new_page)
      @pages << new_page
      if @pages.length > 5
        @pages.shift
      end
    end

    def pop
      return if @pages.empty?
      @pages.delete_at(-1)
    end
  end
end

