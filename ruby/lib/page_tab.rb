module Citronella
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

