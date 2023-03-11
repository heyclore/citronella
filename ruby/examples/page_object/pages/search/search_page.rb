require 'citronella'
require_relative '../contents_page'

class SearchPage < ContentsPage.new.header_menu
  def search_lists
    ui(class: 'gems__gem__name')
  end
end
