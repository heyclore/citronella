require_relative 'contents_page'

class Components
  def search_input
    ui(id: 'home_query', page: ContentsPage.new.search_page)
  end
end
