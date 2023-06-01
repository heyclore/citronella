require 'citronella'
require_relative '../components/header_menu'

class SearchPage
  include HeaderMenu

  def search_lists
    ui(class: 'gems__gem__name')
  end
end
