require_relative 'contents_page'

class SearchPage < ContentsPage.new.components
  def search_lists
    ui(class: 'gems__gem__name')
  end
end
